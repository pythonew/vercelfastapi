from fastapi import FastAPI

app = FastAPI()

@app.get("/example/{parameter}")
def example(parameter: str):
    data = {"Bkash-01847206000":"AG-1",
"Bkash-01878209604":"AG-1",
"Bkash-01613109210":"AG-1",
"Nagad-01847206000":"AG-1",
"nagad-01878209604":"AG-1",
"nagad-01847206419":"AG-1",
"Nagad-01888449221":"AG-1",
"nagad-01890143525":"AG-1",
"Nagad-01881575052":"AG-1",
"Upay-01847206000":"AG-1",
"Upay-01878209604":"AG-1",
"Upay-01890143525":"AG-1",
"Rocket-01847206000":"AG-1",
"Rocket-018884492211":"AG-1",
"Rocket-018815750524":"AG-1",
"Rocket-018210555143":"AG-1",
"Rocket-018901435250":"AG-1",
"Bkash-01889524235":"AG-2",
"Bkash-01891605243":"AG-2",
"Bkash-01856403661":"AG-2",
"Bkash-01825242270":"AG-2",
"Nagad-01874706405":"AG-2",
"Nagad-01888115166":"AG-2",
"Nagad-01619493370":"AG-2",
"nagad-01640684097":"AG-2",
"Upay-01874706405":"AG-2",
"Upay-01888115166":"AG-2",
"Upay01604086349":"AG-2",
"Rocket-018881151666":"AG-2",
"ROCKET016040863490":"AG-2",
"Bkash-01857101415":"AG-3",
"Bkash-01851228855":"AG-3",
"Bkash-01836164143":"AG-3",
"Nagad-01857101415"::"AG-3",
"Bkash-01835671000":"AG-4",
"Bkash-01872517111":"AG-4",
"NAGAD-01835236800":"AG-4",
"Nagad-01886717129":"AG-4",
"NAGAD-01602813737":"AG-4",
"upay-01831915011":"AG-4",
"Upay-01896070152":"AG-4",
"Upay-01835708386":"AG-4",
"UPAY-01835240090":"AG-4",
"rocket-01765226630":"AG-4",
"Rocket-01896070152":"AG-4",
"Rocket-01835708386":"AG-4",
"Rocket-01835240090":"AG-4",
"Bkash-01617231299":"AG-5",
"Bkash-01889281318":"AG-5",
"Bkash-01307144221":"AG-5",
"Nagad-01906449564":"AG-6",
"Rocket-013268768651":"AG-6",
"bkash-01834355324":"AG-8",
"Bkash-01834355463":"AG-8",
"Nagad01616273814":"AG-8",
"Nagad01881561834":"AG-8",
"Nagad01604086348":"AG-8",
"Nagad01834355463":"AG-8",
"Nagad-01640684092":"AG-8",
"Nagad01604086349":"AG-8",
"Upay-01834355324":"AG-8",
"Rocket-018343553242":"AG-8",
"BKASH-01875051820":"AG-9",
"Bkash-01878022203":"AG-10",
"Nagad-01881433185":"AG-10",
"NAGAD-01834355436":"AG-10",
"nagad-01876666760":"AG-10",
"nagad-01856090070":"AG-10",
"Upay-01878022203":"AG-10",
"Rocket-018343553242":"AG-10",
"BKASH-01629291223":"AG-11"}




    agant = data[parameter]
    return agant


@app.get("/")
def main():
    return {
        "message": "Hello my friend"
    }
