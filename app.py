from fastapi import FastAPI

app = FastAPI()

@app.get("/example/{parameter}")
def example(parameter: str):
    data = {"Bkash-01847206000":"ag-1",
"Bkash-01878209604":"ag-1",
"Bkash-01613109210":"ag-1",
"Nagad-01847206000":"ag-1",
"nagad-01878209604":"ag-1",
"nagad-01847206419":"ag-1",
"Nagad-01888449221":"ag-1",
"nagad-01890143525":"ag-1",
"Nagad-01881575052":"ag-1",
"Upay-01847206000":"ag-1",
"Upay-01878209604":"ag-1",
"Upay-01890143525":"ag-1",
"Rocket-01847206000":"ag-1",
"Rocket-018884492211":"ag-1",
"Rocket-018815750524":"ag-1",
"Rocket-018210555143":"ag-1",
"Rocket-018901435250":"ag-1",
"Bkash-01889524235":"ag-2",
"Bkash-01891605243":"ag-2",
"Bkash-01856403661":"ag-2",
"Bkash-01825242270":"ag-2",
"Nagad-01874706405":"ag-2",
"Nagad-01888115166":"ag-2",
"Nagad-01619493370":"ag-2",
"nagad-01640684097":"ag-2",
"Upay-01874706405":"ag-2",
"Upay-01888115166":"ag-2",
"Upay01604086349":"ag-2",
"Rocket-018881151666":"ag-2",
"ROCKET016040863490":"ag-2",
"Bkash-01857101415":"ag-3",
"Bkash-01851228855":"ag-3",
"Bkash-01836164143":"ag-3",
"Nagad-01857101415":"ag-3",
"Bkash-01835671000":"ag-4",
"Bkash-01872517111":"ag-4",
"NAGAD-01835236800":"ag-4",
"Nagad-01886717129":"ag-4",
"NAGAD-01602813737":"ag-4",
"upay-01831915011":"ag-4",
"Upay-01896070152":"ag-4",
"Upay-01835708386":"ag-4",
"UPAY-01835240090":"ag-4",
"rocket-01765226630":"ag-4",
"Rocket-01896070152":"ag-4",
"Rocket-01835708386":"ag-4",
"Rocket-01835240090":"ag-4",
"Bkash-01617231299":"ag-5",
"Bkash-01889281318":"ag-5",
"Bkash-01307144221":"ag-5",
"Nagad-01906449564":"ag-6",
"Rocket-013268768651":"ag-6",
"bkash-01834355324":"ag-8",
"Bkash-01834355463":"ag-8",
"Nagad01616273814":"ag-8",
"Nagad01881561834":"ag-8",
"Nagad01604086348":"ag-8",
"Nagad01834355463":"ag-8",
"Nagad-01640684092":"ag-8",
"Nagad01604086349":"ag-8",
"Upay-01834355324":"ag-8",
"Rocket-018343553242":"ag-8",
"Bkash-01875051820":"ag-9",
"Bkash-01878022203":"ag-10",
"Nagad-01881433185":"ag-10",
"NAGAD-01834355436":"ag-10",
"nagad-01876666760":"ag-10",
"nagad-01856090070":"ag-10",
"Upay-01878022203":"ag-10",
"Rocket-018780222035":"ag-10",
"Rocket-018560900709":"ag-10",
"nagad-01890143525":"ag-1",
"Upay-01878209604":"ag-1",
"BKASH-01878209604":"ag-1",
"Upay-01847206000":"ag-1",
"NAGAG-01890143525":"ag-1",
"Rocket-01765226630":"ag-4",
"Bkash-01872517111":"ag-4",
"bkash-01878022203":"ag-2",
"nagad-01888115166":"ag-2",
}

    try:
        agant = data[parameter]
    except:
        agant = 'NewBank'
    return agant


@app.get("/")
def main():
    return {
        "message": "Hello my friend"
    }
