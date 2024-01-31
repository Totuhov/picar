# picar

[About](about)
[Documentation](documentation)
[Configuration](config.json)

## About

![raspberry](https://img.shields.io/badge/Raspberry%20Pi-A22846?style=for-the-badge&logo=Raspberry%20Pi&logoColor=white "Raspberry Pi") ![linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black "LINUX") ![vscode](https://img.shields.io/badge/VSCode-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white "Visual Studio Code") ![python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue "Python Programming Language") ![plotly](https://img.shields.io/badge/Plotly-239120?style=for-the-badge&logo=plotly&logoColor=white "Plotly") ![dash](https://img.shields.io/badge/dash-008DE4?style=for-the-badge&logo=dash&logoColor=white "Plotly - Dash") ![json](https://img.shields.io/badge/json-5E5C5C?style=for-the-badge&logo=json&logoColor=white "Java Script Object Notation")

## Documentation

### Parcours

1. [Forward and backward](forward_and_backward)
2. [Driving in a circle with maximum steering angle](driving_in_a_circle_with_maximum_steering_angle)
3. [Vorwärtsfahrt bis Hindernis](vorwärtsfahrt_bis_Hindernis)

#### Forward and backward

Das Auto fährt mit langsamer Geschwindigkeit 3 Sekunden geradeaus, stoppt für 1 Sekunde und fährt 3 Sekunden rückwärts.

#### Driving in a circle with maximum steering angle

Das Auto fährt 1 Sekunde geradeaus, dann für 8 Sekunden mit maximalen Lenkwinkel im Uhrzeigersinn und stoppt. Dann soll das Auto diesen Fahrplan in umgekehrter Weise abfahren und an den Ausgangspunkt zurückkehren. Die Vorgehensweise soll für eine Fahrt im entgegengesetzten Uhrzeigersinn wiederholt werden.

#### Vorwärtsfahrt bis Hindernis

Fahren bis ein Hindernis im Weg ist und dann stoppen. Während dieser Fahrt sollen die Fahrdaten und Ultraschall‑Daten aufgezeichnet werden.

### Car Classes

[BaseCar](basecar)
[SonicCar](soniccar)
[SensorCar](sensorcar)

-   ##### BaseCar

**drive_forward**
**drive_backward**
**drive_stop**
**get_direction**

-   ##### SonicCar (inherit from BaseCar)

**distance**
**\_check_low_distance**
**\_check_normal_distance**
**\_check_far_distance**

-   ##### SensorCar (inherit from SonicCar)

### config.json
