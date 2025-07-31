import uuid
from typing import Annotated, Any, List
from uuid import uuid4

from langgraph.graph.message import MessagesState
from pydantic import BaseModel, Field


class Artifact(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))


class TableArtifact(Artifact):
    type: str = "table"
    query: str | None
    result: Any | None


class ChartArtifact(Artifact):
    type: str = "chart"
    query: str | None
    options: Any | None
    vis_script: str | None


class TreeState(MessagesState):
    # The unique ID
    id: uuid.UUID
    # The height of the current node
    height: int
    # The focused sub-problem
    focused_problem: str
    # The maximum initial height for expanding
    max_height: int | None
    # Reason of associating this focused_problem
    # reason_of_associating: Optional[str]
    # Original problem that trigerred this problem
    original_problem: str | None
    # Child list
    child_list: List["TreeState"] | None
    # Responsd to this node as leaf
    respond: str | None
    # Visualization info about this node
    artifact: Annotated[TableArtifact, ChartArtifact] | None
    # Type of Visualization
    artifact_type: str | None
    # Node to be expanded
    expanded_id: uuid.UUID | None
    # Questions asked previously
    prev_questions: List[str] | None
    # Regenerate time record, 0 means no need to regenerate
    regenerate_times: int | None
    # num of subproblems need to generate
    max_subproblems: int | None
    # tables in the dataset
    data_tables: str | None
    # schema of data tables
    data_schemas: dict | None
    # first level subproblems number
    first_level_subproblems: int | None


{
    "id": UUID("4f529efd-2cd1-4e15-9599-12338b87540f"),
    "max_height": 1,
    "focused_problem": "How is the stock situation in the warehouse?",
    "height": 0,
    "prev_questions": ["**How is the stock situation in the warehouse?\n"],
    "regenerate_times": 0,
    "max_subproblems": 4,
    "first_level_subproblems": 2,
    "child_list": [],
}
{"configurable": {"thread_id": "4"}, "recursion_limit": 50}
