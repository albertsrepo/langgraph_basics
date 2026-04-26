from langgraph.graph import START, END, StateGraph
from typing import TypedDict

class State(TypedDict):
    username: str
    frontdesknotes: str
    executivenotes: str
    conclusion: str

def intialassessment(state: State) -> dict:
    print("Due-dilignece about the cancer awareness campaign strategy:", state['username'])
    notes=f"Initial camapaign preparation checklist presenation by {state['username']}. Front desk notes: {state['frontdesknotes']}"
    return {"frontdesknotes": notes}

def executivekeynotes(state: State) -> dict:
    print("Performing executive review and key notes...:", state['username'])
    notes=f"Exec consultation with CMO and stakeholders - Executive notes: {state['executivenotes']}"
    return {"executivenotes": notes}    

def conclusion(state: State) -> dict:
    print("Performing conclusion...state:", state['username'])
    notes=f"Conclusion notes: {state['conclusion']}"
    return {"Conclusion": notes}

builder = StateGraph(State)

builder.add_node("Initial Assessment", intialassessment)
builder.add_node("Executive Key Notes", executivekeynotes)    
builder.add_node("Conclusion", conclusion)

builder.add_edge(START, "Initial Assessment")
builder.add_edge("Initial Assessment", "Executive Key Notes")
builder.add_edge("Executive Key Notes", "Conclusion")
builder.add_edge("Conclusion", END)

# builder.visualize("state_graph.png")

graph=builder.compile()

InitialState = State(
    username="Albert Aboorva",
    frontdesknotes="",
    executivenotes="",
    conclusion=""
)
final_state = graph.invoke(InitialState)
print("Final state:", final_state)  
