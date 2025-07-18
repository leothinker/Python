# pip install -qU "langchain[anthropic]" to call the model

from langgraph.prebuilt import create_react_agent


def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"


agent = create_react_agent(
    model="anthropic:claude-3-7-sonnet-latest",
    tools=[get_weather],
    prompt="You are a helpful assistant",
)

# Run the agent
agent.invoke({"messages": [{"role": "user", "content": "what is the weather in sf"}]})

test = {
    "messages": [
        {
            "content": "请问你是谁？",
            "additional_kwargs": {},
            "response_metadata": {},
            "type": "human",
            "name": None,
            "id": "6b8124de-fb80-4787-8f9a-f13985d3920e",
            "example": False,
        },
        {
            "content": "我是 Annexx，一个专注于商业智能的数据科学助手，擅长处理数据库相关问题和分析业务数据。有什么可以帮助您的吗？",
            "additional_kwargs": {"refusal": None},
            "response_metadata": {
                "token_usage": {
                    "completion_tokens": 33,
                    "prompt_tokens": 1152,
                    "total_tokens": 1185,
                    "completion_tokens_details": {
                        "accepted_prediction_tokens": 0,
                        "audio_tokens": 0,
                        "reasoning_tokens": 0,
                        "rejected_prediction_tokens": 0,
                    },
                    "prompt_tokens_details": {"audio_tokens": 0, "cached_tokens": 0},
                },
                "model_name": "gpt-4o-2024-08-06",
                "system_fingerprint": "fp_ee1d74bde0",
                "id": "chatcmpl-BqpBSTf3RPIJfcFq8J370bhCQQnOE",
                "service_tier": None,
                "prompt_filter_results": [
                    {
                        "prompt_index": 0,
                        "content_filter_results": {
                            "hate": {"filtered": False, "severity": "safe"},
                            "jailbreak": {"filtered": False, "detected": False},
                            "self_harm": {"filtered": False, "severity": "safe"},
                            "sexual": {"filtered": False, "severity": "safe"},
                            "violence": {"filtered": False, "severity": "safe"},
                        },
                    }
                ],
                "finish_reason": "stop",
                "logprobs": None,
                "content_filter_results": {
                    "hate": {"filtered": False, "severity": "safe"},
                    "self_harm": {"filtered": False, "severity": "safe"},
                    "sexual": {"filtered": False, "severity": "safe"},
                    "violence": {"filtered": False, "severity": "safe"},
                },
            },
            "type": "ai",
            "name": None,
            "id": "run--a3e81916-1406-47f8-aed9-ffdb6b169a3c-0",
            "example": False,
            "tool_calls": [],
            "invalid_tool_calls": [],
            "usage_metadata": {
                "input_tokens": 1152,
                "output_tokens": 33,
                "total_tokens": 1185,
                "input_token_details": {"audio": 0, "cache_read": 0},
                "output_token_details": {"audio": 0, "reasoning": 0},
            },
        },
        {
            "content": "请问我叫什么",
            "additional_kwargs": {},
            "response_metadata": {},
            "type": "human",
            "name": None,
            "id": "ae54300f-4054-4c09-8890-215d43d71b60",
            "example": False,
        },
        {
            "content": "对不起，我无法知道你的名字。如果需要，可以告诉我，我会记住的。",
            "additional_kwargs": {"refusal": None},
            "response_metadata": {
                "token_usage": {
                    "completion_tokens": 20,
                    "prompt_tokens": 1195,
                    "total_tokens": 1215,
                    "completion_tokens_details": {
                        "accepted_prediction_tokens": 0,
                        "audio_tokens": 0,
                        "reasoning_tokens": 0,
                        "rejected_prediction_tokens": 0,
                    },
                    "prompt_tokens_details": {"audio_tokens": 0, "cached_tokens": 0},
                },
                "model_name": "gpt-4o-2024-08-06",
                "system_fingerprint": "fp_ee1d74bde0",
                "id": "chatcmpl-BqpC2T4LWKGd2o8DIL67IsmcnNY9Z",
                "service_tier": None,
                "prompt_filter_results": [
                    {
                        "prompt_index": 0,
                        "content_filter_results": {
                            "hate": {"filtered": False, "severity": "safe"},
                            "jailbreak": {"filtered": False, "detected": False},
                            "self_harm": {"filtered": False, "severity": "safe"},
                            "sexual": {"filtered": False, "severity": "safe"},
                            "violence": {"filtered": False, "severity": "safe"},
                        },
                    }
                ],
                "finish_reason": "stop",
                "logprobs": None,
                "content_filter_results": {
                    "hate": {"filtered": False, "severity": "safe"},
                    "self_harm": {"filtered": False, "severity": "safe"},
                    "sexual": {"filtered": False, "severity": "safe"},
                    "violence": {"filtered": False, "severity": "safe"},
                },
            },
            "type": "ai",
            "name": None,
            "id": "run--f77a5f8f-b59d-4b9a-953a-1ac592cd1e0f-0",
            "example": False,
            "tool_calls": [],
            "invalid_tool_calls": [],
            "usage_metadata": {
                "input_tokens": 1195,
                "output_tokens": 20,
                "total_tokens": 1215,
                "input_token_details": {"audio": 0, "cache_read": 0},
                "output_token_details": {"audio": 0, "reasoning": 0},
            },
        },
        {
            "content": "我叫leo",
            "additional_kwargs": {},
            "response_metadata": {},
            "type": "human",
            "name": None,
            "id": "daa5ef59-e0d6-49d6-bdd4-62edd85b3bf6",
            "example": False,
        },
    ],
    "tool_calls": {},
}
