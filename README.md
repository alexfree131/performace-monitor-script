
# Performance Monitor Script

Dieses Python-Skript überwacht die CPU-Temperatur, CPU-Auslastung und RAM-Auslastung und protokolliert die Ergebnisse zweimal am Tag in eine Log-Datei.

## Voraussetzungen

Stellen Sie sicher, dass Sie die folgenden Abhängigkeiten installiert haben:

1. `lm-sensors`:
   ```bash
   sudo apt-get install lm-sensors
   ```
   Führen Sie `sensors-detect` aus und folgen Sie den Anweisungen, um die Sensoren zu konfigurieren.

2. Python-Bibliotheken:
   - `psutil`

## Installation

1. Klonen Sie dieses Repository oder laden Sie die Skript-Datei herunter.
2. Erstellen Sie eine `requirements.txt`-Datei mit folgendem Inhalt:
   ```plaintext
   psutil
   ```
3. Installieren Sie die Python-Abhängigkeiten:
   ```bash
   pip install -r requirements.txt
   ```

## Verwendung

1. Stellen Sie sicher, dass das Skript ausführbar ist:
   ```bash
   chmod +x monitor.py
   ```

2. Starten Sie das Skript im Hintergrund:
   ```bash
   nohup python monitor.py &
   ```

3. Um sicherzustellen, dass das Skript regelmäßig ausgeführt wird, richten Sie einen Cron-Job ein:
   ```bash
   crontab -e
   ```

   Fügen Sie die folgende Zeile hinzu, um das Skript zweimal am Tag (z.B. um 6:00 Uhr und um 18:00 Uhr) auszuführen:
   ```plaintext
   0 6,18 * * * /usr/bin/python3 /path/to/monitor.py
   ```

   Alternativ können Sie einen Shell-Skript-Wrapper verwenden, um sicherzustellen, dass das Python-Skript im Hintergrund läuft und nur einmal zur angegebenen Zeit gestartet wird:

   1. Erstellen Sie eine Datei namens `run_monitor.sh`:
      ```bash
      nano run_monitor.sh
      ```

   2. Fügen Sie den folgenden Inhalt hinzu:
      ```bash
      #!/bin/bash
      nohup /usr/bin/python3 /path/to/monitor.py &
      ```

   3. Machen Sie das Shell-Skript ausführbar:
      ```bash
      chmod +x run_monitor.sh
      ```

   4. Fügen Sie in Ihrer Crontab-Datei eine Zeile hinzu, um das Shell-Skript zweimal täglich auszuführen:
      ```bash
      crontab -e
      ```

      Fügen Sie dann die folgende Zeile hinzu:
      ```plaintext
      0 6,18 * * * /path/to/run_monitor.sh
      ```

## Log-Datei

Die Leistungsdaten werden in eine Datei namens `performance_log.txt` im selben Verzeichnis wie das Skript geschrieben. Jede Zeile enthält einen Zeitstempel, die CPU-Temperatur, die CPU-Auslastung und die RAM-Auslastung.

## Lizenz

Dieses Projekt ist lizenziert unter der MIT-Lizenz. Weitere Informationen finden Sie in der [LICENSE](LICENSE)-Datei.