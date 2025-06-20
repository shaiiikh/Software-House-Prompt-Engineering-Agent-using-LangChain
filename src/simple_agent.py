"""
Simplified Prompt Engineering Agent
Focuses on core functionality without complex LangChain agent framework
"""

from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from typing import Dict, Any, List
import json
import re

from .config import Config
from .prompt_templates import PromptTemplates


class SimplePromptAgent:
    """Simplified prompt engineering agent focusing on core functionality."""
    
    def __init__(self):
        """Initialize the simplified prompt engineering agent."""
        Config.validate()
        
        # Initialize the language model
        self.llm = ChatOpenAI(
            model_name=Config.OPENAI_MODEL_NAME,
            temperature=0.7
        )
    
    def analyze_prompt(self, prompt: str, context: str = "") -> Dict[str, Any]:
        """Analyze a prompt for effectiveness."""
        template = PromptTemplates.PROMPT_ANALYZER
        formatted_prompt = template.format(prompt=prompt, context=context)
        
        response = self.llm.predict(formatted_prompt)
        return self._parse_analysis_response(response)
    
    def optimize_prompt(self, original_prompt: str, issues: str, goal: str) -> str:
        """Optimize a prompt based on identified issues and goals."""
        template = PromptTemplates.PROMPT_OPTIMIZER
        formatted_prompt = template.format(
            original_prompt=original_prompt,
            issues=issues,
            goal=goal
        )
        
        return self.llm.predict(formatted_prompt)
    
    def compare_prompts(self, prompt_a: str, prompt_b: str, test_input: str) -> Dict[str, Any]:
        """Compare two prompts for effectiveness."""
        template = PromptTemplates.AB_TEST_COMPARISON
        formatted_prompt = template.format(
            prompt_a=prompt_a,
            prompt_b=prompt_b,
            test_input=test_input
        )
        
        response = self.llm.predict(formatted_prompt)
        return self._parse_comparison_response(response)
    
    def generate_prompt(self, technique: str, **kwargs) -> str:
        """Generate a prompt using a specific technique."""
        templates = PromptTemplates.get_all_templates()
        
        if technique not in templates:
            raise ValueError(f"Unknown technique: {technique}")
        
        template = templates[technique]
        formatted_prompt = template.format(**kwargs)
        
        return self.llm.predict(formatted_prompt)
    
    def evaluate_response(self, prompt: str, response: str, criteria: str) -> Dict[str, Any]:
        """Evaluate a prompt-response pair."""
        template = PromptTemplates.EVALUATION_METRICS
        formatted_prompt = template.format(
            prompt=prompt,
            response=response,
            criteria=criteria
        )
        
        result = self.llm.predict(formatted_prompt)
        return self._parse_evaluation_response(result)
    
    def optimize_context(self, long_prompt: str, constraints: str) -> str:
        """Optimize a prompt to fit within context constraints."""
        template = PromptTemplates.CONTEXT_OPTIMIZER
        formatted_prompt = template.format(long_prompt=long_prompt, constraints=constraints)
        
        return self.llm.predict(formatted_prompt)
    
    def _parse_analysis_response(self, response: str) -> Dict[str, Any]:
        """Parse the analysis response into structured data."""
        return {
            "analysis": response,
            "clarity_score": self._extract_score(response, "clarity"),
            "specificity_score": self._extract_score(response, "specificity"),
            "suggestions": self._extract_suggestions(response)
        }
    
    def _parse_comparison_response(self, response: str) -> Dict[str, Any]:
        """Parse the comparison response into structured data."""
        return {
            "comparison": response,
            "clearer_prompt": self._extract_clearer_prompt(response),
            "recommendations": self._extract_recommendations(response)
        }
    
    def _parse_evaluation_response(self, response: str) -> Dict[str, Any]:
        """Parse the evaluation response into structured data."""
        return {
            "evaluation": response,
            "overall_score": self._extract_overall_score(response),
            "individual_scores": self._extract_individual_scores(response)
        }
    
    def _extract_score(self, text: str, metric: str) -> int:
        """Extract a score from text."""
        pattern = rf"{metric}.*?(\d+)"
        match = re.search(pattern, text, re.IGNORECASE)
        return int(match.group(1)) if match else 0
    
    def _extract_suggestions(self, text: str) -> List[str]:
        """Extract suggestions from text."""
        suggestions = []
        lines = text.split('\n')
        for line in lines:
            if any(keyword in line.lower() for keyword in ['suggest', 'improve', 'better', 'consider']):
                suggestions.append(line.strip())
        return suggestions
    
    def _extract_clearer_prompt(self, text: str) -> str:
        """Extract which prompt is clearer from comparison text."""
        if "prompt a" in text.lower():
            return "A"
        elif "prompt b" in text.lower():
            return "B"
        return "Unclear"
    
    def _extract_recommendations(self, text: str) -> List[str]:
        """Extract recommendations from comparison text."""
        recommendations = []
        lines = text.split('\n')
        for line in lines:
            if any(keyword in line.lower() for keyword in ['recommend', 'improve', 'better']):
                recommendations.append(line.strip())
        return recommendations
    
    def _extract_overall_score(self, text: str) -> int:
        """Extract overall score from evaluation text."""
        pattern = r"overall.*?(\d+)/50"
        match = re.search(pattern, text, re.IGNORECASE)
        return int(match.group(1)) if match else 0
    
    def _extract_individual_scores(self, text: str) -> Dict[str, int]:
        """Extract individual scores from evaluation text."""
        scores = {}
        metrics = ['relevance', 'completeness', 'accuracy', 'clarity', 'creativity']
        
        for metric in metrics:
            scores[metric] = self._extract_score(text, metric)
        
        return scores 