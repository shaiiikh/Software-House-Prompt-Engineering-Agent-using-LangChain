from langchain.prompts import PromptTemplate
from typing import Dict, List

class PromptTemplates:
    """Collection of prompt templates for different prompt engineering techniques."""
    
    # Basic prompt engineering templates
    ZERO_SHOT = PromptTemplate(
        input_variables=["task", "input_text"],
        template="""Task: {task}

Input: {input_text}

Please provide a response:"""
    )
    
    FEW_SHOT = PromptTemplate(
        input_variables=["task", "examples", "input_text"],
        template="""Task: {task}

Examples:
{examples}

Input: {input_text}

Please provide a response:"""
    )
    
    CHAIN_OF_THOUGHT = PromptTemplate(
        input_variables=["task", "input_text"],
        template="""Task: {task}

Input: {input_text}

Let's approach this step by step:

1. First, let me understand what needs to be done...
2. Then, I'll consider the key factors...
3. Finally, I'll provide the answer...

Answer:"""
    )
    
    ROLE_BASED = PromptTemplate(
        input_variables=["role", "task", "input_text"],
        template="""You are an expert {role}.

Task: {task}

Input: {input_text}

As a {role}, please provide your response:"""
    )
    
    # Prompt optimization templates
    PROMPT_ANALYZER = PromptTemplate(
        input_variables=["prompt", "context"],
        template="""Analyze the following prompt for effectiveness and potential improvements:

Prompt: {prompt}
Context: {context}

Please provide:
1. Clarity assessment (1-10)
2. Specificity assessment (1-10)
3. Potential ambiguities
4. Suggested improvements
5. Alternative formulations"""
    )
    
    PROMPT_OPTIMIZER = PromptTemplate(
        input_variables=["original_prompt", "issues", "goal"],
        template="""Original Prompt: {original_prompt}

Identified Issues: {issues}
Optimization Goal: {goal}

Please provide an improved version of this prompt that addresses the issues and achieves the goal:"""
    )
    
    # A/B testing template
    AB_TEST_COMPARISON = PromptTemplate(
        input_variables=["prompt_a", "prompt_b", "test_input"],
        template="""Compare the effectiveness of these two prompts:

Prompt A: {prompt_a}
Prompt B: {prompt_b}

Test Input: {test_input}

Please evaluate:
1. Which prompt is clearer?
2. Which prompt is more specific?
3. Which prompt is likely to produce better results?
4. Specific improvements for each prompt"""
    )
    
    # Context window optimization
    CONTEXT_OPTIMIZER = PromptTemplate(
        input_variables=["long_prompt", "constraints"],
        template="""Optimize this prompt to fit within context constraints while maintaining effectiveness:

Original Prompt: {long_prompt}
Constraints: {constraints}

Please provide:
1. A condensed version that maintains key information
2. Alternative approaches to reduce length
3. Priority ranking of prompt elements"""
    )
    
    # Prompt engineering for specific domains
    CREATIVE_WRITING = PromptTemplate(
        input_variables=["genre", "style", "topic", "length"],
        template="""Write a {genre} piece in {style} style about {topic}.

Requirements:
- Length: {length}
- Maintain consistent tone and style
- Include engaging elements appropriate for the genre

Please create the content:"""
    )
    
    TECHNICAL_WRITING = PromptTemplate(
        input_variables=["topic", "audience", "complexity", "format"],
        template="""Create {format} content about {topic}.

Target Audience: {audience}
Complexity Level: {complexity}

Requirements:
- Use clear, precise language
- Include relevant technical details
- Structure for easy comprehension
- Include examples where helpful

Please create the content:"""
    )
    
    # Prompt evaluation metrics
    EVALUATION_METRICS = PromptTemplate(
        input_variables=["prompt", "response", "criteria"],
        template="""Evaluate the following prompt-response pair:

Prompt: {prompt}
Response: {response}
Evaluation Criteria: {criteria}

Please rate on a scale of 1-10:
1. Relevance: How well does the response address the prompt?
2. Completeness: Does the response cover all aspects of the prompt?
3. Accuracy: Is the information provided correct?
4. Clarity: Is the response clear and well-structured?
5. Creativity: Does the response show appropriate creativity?

Overall Score: __/50
Comments:"""
    )

    @classmethod
    def get_all_templates(cls) -> Dict[str, PromptTemplate]:
        """Get all available prompt templates."""
        return {
            "zero_shot": cls.ZERO_SHOT,
            "few_shot": cls.FEW_SHOT,
            "chain_of_thought": cls.CHAIN_OF_THOUGHT,
            "role_based": cls.ROLE_BASED,
            "prompt_analyzer": cls.PROMPT_ANALYZER,
            "prompt_optimizer": cls.PROMPT_OPTIMIZER,
            "ab_test_comparison": cls.AB_TEST_COMPARISON,
            "context_optimizer": cls.CONTEXT_OPTIMIZER,
            "creative_writing": cls.CREATIVE_WRITING,
            "technical_writing": cls.TECHNICAL_WRITING,
            "evaluation_metrics": cls.EVALUATION_METRICS,
        } 