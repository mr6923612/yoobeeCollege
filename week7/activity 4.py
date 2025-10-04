
from abc import ABC, abstractmethod

@abstractmethod
class traffic_Strategy:

    def travel(self, distance: float) -> None:
        pass

class CarTravel(traffic_Strategy):

    def travel(self, distance: float) -> None:
        print(f"Traveling {distance} miles by Car.")

class shipTravel(traffic_Strategy):

    def travel(self, distance: float) -> None:
        print(f"Traveling {distance} miles by Ship.")

class busTravel(traffic_Strategy):

    def travel(self, distance: float) -> None:
        print(f"Traveling {distance} miles by Bus.")

class travelFactory:


    def get_travel_mode(self, mode: str) -> traffic_Strategy:
        if mode == "car":
            return CarTravel()
        elif mode == "ship":
            return shipTravel()
        elif mode == "bus":
            return busTravel()
        else:
            raise ValueError(f"Unknown travel mode: {mode}")
        
# Example usage
if __name__ == "__main__":
    distance = 150.0
    mode = "car"  # This could be dynamic based on user input

    travel_factory = travelFactory()
    travel_mode = travel_factory.get_travel_mode(mode)
    travel_mode.travel(distance)
