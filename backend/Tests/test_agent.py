from graph.workflow import build_graph

agent = build_graph()

result = agent.invoke(
    {
        "user_input":
        "What should I learn for a Generative AI Engineer role?"
    }
)

print(result)