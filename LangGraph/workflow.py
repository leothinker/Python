from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List, Literal, Sequence, cast
from zoneinfo import ZoneInfo

from langchain.chat_models import init_chat_model
from langchain_core.messages import AIMessage, AnyMessage
from langgraph.graph import StateGraph, add_messages
from langgraph.managed import IsLastStep
from langgraph.prebuilt import ToolNode
from typing_extensions import Annotated

from configuration import Configuration
from tools import TOOLS


@dataclass
class InputState:
    messages: Annotated[Sequence[AnyMessage], add_messages] = field(default_factory=list)


@dataclass
class State(InputState):
    is_last_step: IsLastStep = field(default=False)


llm = init_chat_model(
    "azure_openai:gpt-4o",
    temperature=0,
)


async def call_model(state: State) -> Dict[str, List[AIMessage]]:
    configuration = Configuration.from_context()

    model = init_chat_model("azure_openai:gpt-4o", temperature=0).bind_tools(TOOLS)

    system_message = configuration.system_prompt.format(
        dialect="MySQL",
        limit=1000,
        time=datetime.now(ZoneInfo("Asia/Shanghai")).isoformat(),
    )

    response = cast(
        AIMessage,
        await model.ainvoke([{"role": "system", "content": system_message}, *state.messages]),
    )

    if state.is_last_step and response.tool_calls:
        return {
            "messages": [
                AIMessage(
                    id=response.id,
                    content="Sorry, I could not find an answer to your question in the specified number of steps.",
                )
            ]
        }

    return {"messages": [response]}


# Build workflow
builder = StateGraph(State)

# Add nodes
builder.add_node(call_model)
builder.add_node("tools", ToolNode(TOOLS))


builder.add_edge("__start__", "call_model")


def route_model_output(state: State) -> Literal["__end__", "tools"]:
    last_message = state.messages[-1]
    if not isinstance(last_message, AIMessage):
        raise ValueError(
            f"Expected AIMessage in output edges, but got {type(last_message).__name__}"
        )
    if not last_message.tool_calls:
        return "__end__"
    return "tools"


builder.add_conditional_edges(
    "call_model",
    route_model_output,
)

builder.add_edge("tools", "call_model")


graph = builder.compile(name="ReAct Agent")
