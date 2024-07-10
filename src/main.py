from dotenv import load_dotenv
from crewai import Crew
from tasks import Field_Tasks
from agents import Field_Agents
import sys

def main(field):
    load_dotenv()
    
    print(f"## Welcome to the {field.capitalize()} Landscape Crew")
    print('-------------------------------')

    tasks = Field_Tasks(field)
    agents = Field_Agents(field)
    
    research_agent = agents.research_agent()
    industry_analysis_agent = agents.industry_analysis_agent()
    innovation_strategy_agent = agents.innovation_strategy_agent()
    summary_and_briefing_agent = agents.summary_and_briefing_agent()
    
    # create tasks
    research_task = tasks.research_task(research_agent)
    industry_analysis_task = tasks.industry_analysis_task(industry_analysis_agent)
    innovation_strategy_task = tasks.innovation_strategy_task(innovation_strategy_agent)
    summary_and_briefing_task = tasks.summary_and_briefing_task(summary_and_briefing_agent)
    
    innovation_strategy_task.context = [research_task, industry_analysis_task]
    summary_and_briefing_task.context = [research_task, industry_analysis_task, innovation_strategy_task]
    
    crew = Crew(
        agents=[
            research_agent,
            industry_analysis_agent,
            innovation_strategy_agent,
            summary_and_briefing_agent
        ],
        tasks=[
            research_task,
            industry_analysis_task,
            innovation_strategy_task,
            summary_and_briefing_task
        ]
    )

    result = crew.kickoff()
    
    print(f"Here is the recent {field} landscape analysis:")
    print(result)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a field to analyze. Example: python main.py 'artificial intelligence'")
        sys.exit(1)
    
    field = sys.argv[1]
    main(field)