"""
Software House Prompt Engineering Agent
Specialized for software development, project management, and client communication
"""

from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from typing import Dict, Any, List
import json
import re

from .config import Config
from .prompt_templates import PromptTemplates


class SoftwareHouseAgent:
    """Specialized prompt engineering agent for software house operations."""
    
    def __init__(self):
        """Initialize the software house agent."""
        Config.validate()
        
        # Initialize the language model
        self.llm = ChatOpenAI(
            model_name=Config.OPENAI_MODEL_NAME,
            temperature=0.7
        )
    
    def generate_technical_spec(self, project_type: str, requirements: str, tech_stack: str = "") -> str:
        """Generate technical specifications for software projects."""
        template = PromptTemplate(
            input_variables=["project_type", "requirements", "tech_stack"],
            template="""As a senior software architect, create a comprehensive technical specification for a {project_type} project.

Client Requirements: {requirements}
Preferred Tech Stack: {tech_stack}

Please provide:
1. System Architecture Overview
2. Database Design
3. API Specifications
4. Security Considerations
5. Performance Requirements
6. Deployment Strategy
7. Timeline Estimation
8. Resource Requirements

Format the response in a professional, client-ready document structure."""
        )
        
        formatted_prompt = template.format(
            project_type=project_type,
            requirements=requirements,
            tech_stack=tech_stack
        )
        
        return self.llm.predict(formatted_prompt)
    
    def create_project_proposal(self, client_name: str, project_scope: str, budget_range: str) -> str:
        """Generate professional project proposals for clients."""
        template = PromptTemplate(
            input_variables=["client_name", "project_scope", "budget_range"],
            template="""Create a professional project proposal for {client_name}.

Project Scope: {project_scope}
Budget Range: {budget_range}

Include:
1. Executive Summary
2. Project Overview
3. Technical Approach
4. Deliverables
5. Timeline & Milestones
6. Team Structure
7. Pricing Breakdown
8. Risk Mitigation
9. Next Steps

Make it compelling, professional, and tailored to win the project."""
        )
        
        formatted_prompt = template.format(
            client_name=client_name,
            project_scope=project_scope,
            budget_range=budget_range
        )
        
        return self.llm.predict(formatted_prompt)
    
    def generate_code_documentation(self, code_snippet: str, language: str, purpose: str) -> str:
        """Generate comprehensive code documentation."""
        template = PromptTemplate(
            input_variables=["code_snippet", "language", "purpose"],
            template="""Generate professional documentation for this {language} code:

Code:
{code_snippet}

Purpose: {purpose}

Please provide:
1. Function/Class Overview
2. Parameters & Return Values
3. Usage Examples
4. Dependencies
5. Performance Notes
6. Best Practices
7. Testing Recommendations

Format as clean, maintainable documentation suitable for a development team."""
        )
        
        formatted_prompt = template.format(
            code_snippet=code_snippet,
            language=language,
            purpose=purpose
        )
        
        return self.llm.predict(formatted_prompt)
    
    def create_client_communication(self, situation: str, client_type: str, tone: str) -> str:
        """Generate professional client communication messages."""
        template = PromptTemplate(
            input_variables=["situation", "client_type", "tone"],
            template="""Create a professional {tone} communication for a {client_type} client.

Situation: {situation}

Requirements:
- Professional and clear
- Appropriate for {client_type} client
- {tone} tone
- Actionable next steps
- Maintains positive relationship

Include:
1. Clear subject line
2. Professional greeting
3. Situation explanation
4. Proposed solution/action
5. Timeline if applicable
6. Call to action
7. Professional closing"""
        )
        
        formatted_prompt = template.format(
            situation=situation,
            client_type=client_type,
            tone=tone
        )
        
        return self.llm.predict(formatted_prompt)
    
    def generate_test_cases(self, feature_description: str, testing_type: str) -> str:
        """Generate comprehensive test cases for software features."""
        template = PromptTemplate(
            input_variables=["feature_description", "testing_type"],
            template="""Create comprehensive {testing_type} test cases for this feature:

Feature: {feature_description}

Please provide:
1. Test Case ID
2. Test Description
3. Preconditions
4. Test Steps
5. Expected Results
6. Test Data Requirements
7. Priority Level
8. Assumptions

Cover:
- Happy path scenarios
- Edge cases
- Error conditions
- Performance considerations
- Security aspects

Format as a structured test plan document."""
        )
        
        formatted_prompt = template.format(
            feature_description=feature_description,
            testing_type=testing_type
        )
        
        return self.llm.predict(formatted_prompt)
    
    def create_development_estimate(self, task_description: str, complexity_level: str, team_size: str) -> Dict[str, Any]:
        """Generate development time and resource estimates."""
        template = PromptTemplate(
            input_variables=["task_description", "complexity_level", "team_size"],
            template="""Provide a detailed development estimate for this task:

Task: {task_description}
Complexity: {complexity_level}
Team Size: {team_size}

Please estimate:
1. Development Hours
2. Testing Hours
3. Documentation Hours
4. Review Hours
5. Total Timeline
6. Required Skills
7. Risk Factors
8. Dependencies

Provide estimates in a structured format with reasoning."""
        )
        
        formatted_prompt = template.format(
            task_description=task_description,
            complexity_level=complexity_level,
            team_size=team_size
        )
        
        response = self.llm.predict(formatted_prompt)
        return self._parse_estimate_response(response)
    
    def generate_deployment_guide(self, project_name: str, environment: str, tech_stack: str) -> str:
        """Generate deployment and setup guides."""
        template = PromptTemplate(
            input_variables=["project_name", "environment", "tech_stack"],
            template="""Create a comprehensive deployment guide for {project_name}.

Environment: {environment}
Tech Stack: {tech_stack}

Include:
1. Prerequisites
2. Environment Setup
3. Installation Steps
4. Configuration
5. Database Setup
6. Security Configuration
7. Monitoring Setup
8. Troubleshooting
9. Rollback Procedures

Make it step-by-step and suitable for DevOps teams."""
        )
        
        formatted_prompt = template.format(
            project_name=project_name,
            environment=environment,
            tech_stack=tech_stack
        )
        
        return self.llm.predict(formatted_prompt)
    
    def create_project_status_report(self, project_name: str, current_status: str, milestones: str) -> str:
        """Generate professional project status reports."""
        template = PromptTemplate(
            input_variables=["project_name", "current_status", "milestones"],
            template="""Create a professional project status report for {project_name}.

Current Status: {current_status}
Key Milestones: {milestones}

Include:
1. Executive Summary
2. Progress Overview
3. Completed Deliverables
4. Current Sprint Status
5. Upcoming Milestones
6. Risks & Issues
7. Resource Utilization
8. Budget Status
9. Next Steps

Format as a client-ready status report."""
        )
        
        formatted_prompt = template.format(
            project_name=project_name,
            current_status=current_status,
            milestones=milestones
        )
        
        return self.llm.predict(formatted_prompt)
    
    def generate_technical_interview_questions(self, position: str, skill_level: str, focus_areas: str) -> str:
        """Generate technical interview questions for hiring."""
        template = PromptTemplate(
            input_variables=["position", "skill_level", "focus_areas"],
            template="""Create technical interview questions for a {position} position.

Skill Level: {skill_level}
Focus Areas: {focus_areas}

Include:
1. Programming Fundamentals
2. Problem-Solving Questions
3. System Design Questions
4. Database Questions
5. Framework-Specific Questions
6. Behavioral Questions
7. Code Review Scenarios
8. Expected Answers/Rubric

Structure as a comprehensive interview guide."""
        )
        
        formatted_prompt = template.format(
            position=position,
            skill_level=skill_level,
            focus_areas=focus_areas
        )
        
        return self.llm.predict(formatted_prompt)
    
    def _parse_estimate_response(self, response: str) -> Dict[str, Any]:
        """Parse the estimate response into structured data."""
        # Extract key metrics from the response
        hours_pattern = r"(\d+)\s*hours?"
        timeline_pattern = r"(\d+)\s*(?:days?|weeks?)"
        
        dev_hours = re.findall(hours_pattern, response.lower())
        timeline = re.findall(timeline_pattern, response.lower())
        
        return {
            "raw_response": response,
            "estimated_hours": int(dev_hours[0]) if dev_hours else 0,
            "timeline_days": int(timeline[0]) if timeline else 0,
            "complexity_analysis": self._extract_complexity_analysis(response)
        }
    
    def _extract_complexity_analysis(self, text: str) -> str:
        """Extract complexity analysis from estimate response."""
        complexity_keywords = ["simple", "moderate", "complex", "high", "low"]
        for keyword in complexity_keywords:
            if keyword in text.lower():
                return keyword.capitalize()
        return "Moderate" 