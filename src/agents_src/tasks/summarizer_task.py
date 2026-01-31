from crewai import Task
from pydantic import BaseModel
from src.agents_src.agents.summarizer_agent import summarizer_agent
from src.agents_src.tasks.question_answer_task import qa_task


class FinalAnswer(BaseModel):
    summary: str
    key_points: list[str]
    sources: list[str]
    evidence: list[dict]


summarizer_task = Task(
    agent=summarizer_agent,
    name="Summarizer Task",
    description="""
You will receive a package from the previous task.
- Summarize only the EVIDENCE.
- Use only the provided evidence snippets.
- Create clear bullet points that every bullet must be supported by an evidence snippet. 
- Keep citations (sources) unchanged.
- DO NOT add any external knowledge.
""",
    expected_output="""
Return a JSON file:
{
"summary": "Short clear answer grounded in the answer",
"key_points": Some clear bullet points,
"sources": citations,
"snippet": [
        {
          "text": "Exact quote from document",
          "source": "filename",
          "page": "page number",
        }
      ],
}
""",
    context=[qa_task],
    output_pydantic=FinalAnswer
)
