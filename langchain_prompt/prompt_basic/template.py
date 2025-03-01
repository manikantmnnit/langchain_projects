from  langchain_core.prompts import PromptTemplate

# Template
template=PromptTemplate(
    template="""Act as a research assistant and provide an explanation of the {topic_input} library. Ensure the explanation follows these guidelines:

Explanation Style: {style_input}

If 'Basic Introduction', provide a clear and concise overview of the library.

If 'Explain with real example', include a practical example or use case.

If 'Explain with code', provide a code snippet with comments to demonstrate its usage.

If 'Explain with Math logic', include mathematical formulations or logic behind the library's functionality.

Explanation Length: {length_input}

If '2-3 sentences', keep the explanation brief and to the point.

If '2-3 paragraphs', provide a moderately detailed explanation.

If 'long explanation', include a comprehensive breakdown with examples, code, or math as needed.

Additional Details:

Highlight the key features or functionalities of the {topic_input} library.

If applicable, explain how it compares to similar libraries or tools.

Use simple and clear language to ensure the explanation is accessible to beginners.""",
input_variables=['topic_input','length_input','style_input']
)

template.save('template.json')
template.save('template.yaml')
template.save('template.txt')
    
