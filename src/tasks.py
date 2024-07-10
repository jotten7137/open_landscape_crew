from textwrap import dedent
from crewai import Task
from datetime import date

today = date.today()

class Field_Tasks:
    def __init__(self, field):
        self.field = field

    def research_task(self, agent):
        return Task(
            description=dedent(f"""\
                Identify the next big trend in {self.field} based on current developments and future projections.
                Consider advancements in relevant subfields and technologies within {self.field}.
                Analyze recent research papers, industry reports, and expert opinions published within the last 6 months.
                Focus on emerging technologies and methodologies that have the potential to significantly impact the {self.field} landscape in the next 1-3 years.
                Also consider how AI and other cutting-edge technologies are influencing {self.field}.
                Current date: {today}
                """),
            expected_output=dedent(f"""\
                A detailed report summarizing:
                1. Current state of {self.field} as of {today}
                2. Analysis of 3-5 emerging trends in {self.field}
                3. Prediction of the most likely "next big trend" with supporting evidence
                4. Potential impact of this trend on various industries and society
                5. Timeline for expected mainstream adoption
                6. Key players and companies driving this trend
                7. Potential challenges or ethical considerations
                8. References to relevant research papers, reports, or expert opinions
                9. Analysis of how AI is impacting or could impact these trends in {self.field}
                """),
            agent=agent,
            async_execution=True
        )
    
    def industry_analysis_task(self, agent):
        return Task(
            description=dedent(f"""\
                Conduct a comprehensive analysis of the {self.field} industry as of {today}.
                Focus on the following key areas:
                1. Current market trends: Identify and analyze the top 3-5 trends shaping the {self.field} industry.
                2. Market size and growth: Provide current market size estimates and growth projections for the next 5 years.
                3. Key players: Identify major companies, startups, and research institutions driving innovation.
                4. Technological advancements: Highlight recent breakthroughs in {self.field}, including relevant AI applications.
                5. Industry challenges: Analyze technical, ethical, and regulatory challenges facing the {self.field} industry.
                6. Opportunities: Identify emerging opportunities for {self.field} applications across various sectors.
                7. Investment landscape: Summarize recent funding trends, major investments, and M&A activities.
                8. Geographical analysis: Compare {self.field} development and adoption across different regions globally.
                
                Base your analysis on reputable market reports, academic publications, industry news, and expert opinions from the past 12 months.
                """),
            expected_output=dedent(f"""\
                A comprehensive {self.field} industry analysis report including:
                1. Executive summary of key findings
                2. Detailed analysis of each focus area mentioned in the task description
                3. SWOT (Strengths, Weaknesses, Opportunities, Threats) analysis of the {self.field} industry
                4. Future outlook: Short-term (1-2 years) and long-term (3-5 years) predictions for the industry
                5. Recommendations for stakeholders (e.g., investors, policymakers, businesses)
                6. Visual aids: Charts, graphs, or infographics to illustrate key points
                7. List of sources and references used in the analysis
                8. Analysis of AI's current and potential future impact on the {self.field} industry
                
                The report should be insightful, data-driven, and provide actionable intelligence for decision-makers in the {self.field} space.
                """),
            async_execution=True,
            agent=agent
        )
    
    def innovation_strategy_task(self, agent):
        return Task(
            description=dedent(f"""\
                Develop a comprehensive innovation strategy framework for a {self.field}-focused technology company.
                The framework should include:
                1. Key innovation areas: Identify 3-5 critical areas for innovation based on current {self.field} trends and market demands.
                2. Strategic talking points: Develop concise, impactful statements that articulate the company's innovation vision and approach.
                3. Discussion angles: Create thought-provoking perspectives on {self.field} innovation to stimulate strategic conversations.
                4. Probing questions: Formulate insightful questions to uncover opportunities, challenges, and unexplored areas in {self.field} innovation.
                5. Stakeholder considerations: Address how the innovation strategy impacts different stakeholders (e.g., employees, customers, investors, partners).
                6. Resource allocation: Suggest how to balance resources between incremental improvements and disruptive innovations.
                7. Innovation metrics: Propose key performance indicators (KPIs) to measure the success of innovation initiatives.
                8. Competitive analysis: Include points on how this strategy positions the company against competitors.
                9. AI integration: Discuss how AI can be leveraged to drive innovation in {self.field}.

                Base your strategy on current {self.field} industry trends, successful innovation models, and forward-thinking approaches in technology leadership.
                """),
            expected_output=dedent(f"""\
                A detailed innovation strategy report for {self.field} including:
                1. Executive summary of the innovation framework
                2. List of key innovation areas with brief justifications
                3. 10-15 strategic talking points for leadership communication
                4. 5-7 unique discussion angles to drive strategic conversations
                5. 20-25 probing questions categorized by innovation area
                6. Stakeholder impact analysis and engagement strategies
                7. Proposed resource allocation model for innovation initiatives
                8. Set of innovation KPIs and measurement methodologies
                9. Competitive positioning analysis in the context of the innovation strategy
                10. Implementation roadmap with short-term and long-term objectives
                11. Potential risks and mitigation strategies for the proposed innovation approach
                12. Strategies for AI integration in {self.field} innovation

                The report should be actionable, forward-thinking, and aligned with cutting-edge {self.field} developments and business strategy best practices.
                """),
            agent=agent
        )
    
    def summary_and_briefing_task(self, agent):
        return Task(
            description=dedent(f"""\
                Compile all research findings, industry analysis, and strategic insights into a comprehensive, 
                well-structured standard report. The report should synthesize information from previous tasks 
                and present a coherent overview of the {self.field} industry, trends, and strategic recommendations.
                
                Ensure the report is clear, concise, and provides actionable insights for decision-makers.
                
                Current date: {today}
                """),
            expected_output=dedent(f"""\
                A comprehensive standard report on {self.field} with the following structure:

                1. Executive Summary (1 page)
                - Key findings and recommendations

                2. Table of Contents

                3. Introduction (1-2 pages)
                - Purpose of the report
                - Methodology
                - Current {self.field} landscape overview

                4. {self.field.capitalize()} Industry Analysis (3-4 pages)
                - Market size and growth projections
                - Key players and competitive landscape
                - Regional analysis

                5. Current {self.field.capitalize()} Trends (3-4 pages)
                - Top 5 current trends with brief explanations
                - Potential impact on various industries

                6. Emerging Technologies (2-3 pages)
                - Breakthrough technologies in {self.field}
                - Potential applications and impact
                - Role of AI in advancing {self.field}

                7. Challenges and Opportunities (2-3 pages)
                - Technical challenges
                - Ethical and regulatory considerations
                - Emerging opportunities in {self.field}

                8. Strategic Recommendations (2-3 pages)
                - Short-term actions (next 12 months)
                - Long-term strategies (2-5 years)
                - Innovation focus areas

                9. Future Outlook (1-2 pages)
                - Predictions for {self.field} development in the next 3-5 years
                - Potential disruptive scenarios

                10. Appendices
                    - Glossary of key {self.field} terms
                    - List of key {self.field} companies to watch
                    - Recent {self.field.capitalize()} News Headlines with URL links (last 30 days)
                    - Selected {self.field} research articles with brief summaries and URL links (last 6 months)

                11. References

                The report should be 20-25 pages in total (excluding appendices and references), 
                use clear and professional language, and include relevant charts, graphs, or 
                infographics to illustrate key points. Ensure all information is up-to-date as of {today}.
                """),
            agent=agent,
            output_file=f'outputs/{self.field}_summary_{today}.txt'
        )