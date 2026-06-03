# Datensatzauswahl – Begründung

## 1. Gewählter Datensatz: CICEVSE2024 (EVSE-B)

* **Grund:** Es besteht eine **hohe Feature-Überschneidung** mit dem *ReSiLENT-System*. 
    * **Power Consumption Features:** `shunt_voltage`, `bus_voltage_V`, `current_mA` und `power_mW` sind 1:1 identisch.
    * **HPC- und Kernel-Features:** auch eine hohe überschneidung vor allem die HPC-Events
    * **Fazit:** Dieser Datensatz bietet die direkteste Basis für eine realitätsnahe Evaluation.
* **Synthetische Erweiterung:** Da nur *EVSE-B* vollständige Feature-Daten liefert, werden $N$ weitere Knoten durch kontrolliertes Resampling mit *Gaussian Noise* erzeugt. Die zeitliche Synchronisation ist dabei gewährleistet, da alle Knoten von denselben Zeitstempeln (*Timestamps*) abgeleitet werden.

---

## 2. Abgelehnte Datensätze

### CICEV2023
* **Problem:** Nur 3 von 53 *Charge Stations (CSs)* besitzen `perf stat`-Daten.
* **Einschränkung:** Es sind lediglich 3 Features vorhanden (`branch`, `cycles`, `instructions`).
* **Fazit:** Die Feature-Basis ist zu schmal für einen aussagekräftigen Aggregationsansatz.

### CICIoT23 / ToN-IoT / UNSW-NB15
Hierbei handelt es sich um netzwerkflow-basierte Datensätze (`pcap`/`NetFlow`). Diese sind aus drei wesentlichen Gründen **ungeeignet**:

1.  **Falsche Domäne:** Netzwerkflow-Features haben keine semantische Entsprechung in einer physikalischen Ladeinfrastruktur.
2.  **Semantische Heterogenität:** Flows auf demselben Knoten haben unterschiedliche Ursachen. Eine Aggregation über Knoten hinweg erzeugt daher bedeutungslose Mittelwerte.
3.  **Fehlende physikalische Vergleichbarkeit:** Mein Aggregationsansatz setzt voraus, dass alle Knoten dieselben Metriken messen. Diese Datensätze wurden für klassische *NIDS-Szenarien* (Network Intrusion Detection Systems) entwickelt – nicht für die kollaborative Anomalieerkennung in physikalisch homogenen IoT-Infrastrukturen.
