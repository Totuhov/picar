# picar
-   **[Important Tips](#tips)**

-   **[About](#about)**

-   **[Documentation](#documentation)**

-   **[Configuration](#configjson)**

## Tips

1. Importing modules from different file locations
go tho the main file where the modules should be imporded
open Terminal
navigate to the desired location witch should be imported

"pwd" to get the location

export PYTHONPATH=/home/nikolay/picar/{location}:${PYTHONPATH}

now you have this location into system's paths
more information on https://www.youtube.com/watch?v=HNChkuE6HyA

## About

![raspberry](https://img.shields.io/badge/Raspberry%20Pi-A22846?style=for-the-badge&logo=Raspberry%20Pi&logoColor=white "Raspberry Pi") ![linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black "LINUX") ![vscode](https://img.shields.io/badge/VSCode-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white "Visual Studio Code") ![python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue "Python Programming Language") ![plotly](https://img.shields.io/badge/Plotly-239120?style=for-the-badge&logo=plotly&logoColor=white "Plotly") ![dash](https://img.shields.io/badge/dash-008DE4?style=for-the-badge&logo=dash&logoColor=white "Plotly - Dash") ![pandas](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white "Pandas Library") ![json](https://img.shields.io/badge/json-5E5C5C?style=for-the-badge&logo=json&logoColor=white "Java Script Object Notation")

## Documentation

### Parcours

1. [Forward and backward](#1-forward-and-backward)
2. [Driving in a circle with maximum steering angle](#2-driving-in-a-circle-with-maximum-steering-angle)
3. [Vorwärtsfahrt bis Hindernis](#3-vorwärtsfahrt-bis-hindernis)
4. [Erkundungstour](#4-erkundungstour)
5. [Linieverfolgung](#5-linieverfolgung)
6. [Hindernis‑Umfahrung](#6-hindernis‑umfahrung)

#### 1. Forward and backward

Das Auto fährt mit langsamer Geschwindigkeit 3 Sekunden geradeaus, stoppt für 1 Sekunde und fährt 3 Sekunden rückwärts.

#### 2. Driving in a circle with maximum steering angle

Das Auto fährt 1 Sekunde geradeaus, dann für 8 Sekunden mit maximalen Lenkwinkel im Uhrzeigersinn und stoppt. Dann soll das Auto diesen Fahrplan in umgekehrter Weise abfahren und an den Ausgangspunkt zurückkehren. Die Vorgehensweise soll für eine Fahrt im entgegengesetzten Uhrzeigersinn wiederholt werden.

#### 3. Vorwärtsfahrt bis Hindernis

Fahren bis ein Hindernis im Weg ist und dann stoppen. Während dieser Fahrt sollen die Fahrdaten und Ultraschall‑Daten aufgezeichnet werden.

#### 4. Erkundungstour

Das Auto fährt, und im Falle eines Hindernisses ändert es die Fahrtrichtung, um die Fahrt fortzusetzen. Für die Änderung der Fahrtrichtung wird ein maximaler Lenkwinkel eingeschlagen, und das Fahrzeug kann auch rückwärts fahren. Die Geschwindigkeit, der Abstand zum Objekt und die Fahrtrichtung werden regelmäßig gespeichert. Die Fahrdaten werden aufgezeichnet.

#### 5. Linieverfolgung

Folgen einer Linie auf dem Boden.

#### 6. Linieverfolgung bis zur Hindernisserkennung

Kombination von Linienverfolgung per Infrarot‑Senor und Hinderniserkennung per Ultraschall‑Sensor. Das Auto soll einer Linie folgen bis ein Hindernis erkannt wird und dann anhalten.

#### 7. Hindernis‑Umfahrung

Entwicklung und Testen einer Hindernis‑Umfahrung basieren auf der Linienverfolgung. Das Hindernis blockiert die Linie und soll umfahren werden.

### Car Classes

-   #### BaseCar

    *drive_forward*

    *drive_backward*

    *drive_stop*

    *get_direction*

-   #### SonicCar (inherit from BaseCar)

    *distance*

    *\_check_low_distance*

    *\_check_normal_distance*

    *\_check_far_distance*

-   #### SensorCar (inherit from SonicCar)

    *obsticle_detected_mode*

    *turn*

### config.json
