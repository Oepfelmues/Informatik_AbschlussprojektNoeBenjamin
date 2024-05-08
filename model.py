import torch                    # Import Torch importiert die PYtorch Bilibliothek, welche vorallem für das Machine-learning verwendet wird. (z.B. torch.tensor() um  Numpy arrays in Tensore zu konvertiern)
import torch.nn as nn           # Hier wird das Modul nn aus PyTorch importiert. nn enthält verschiedene Funktionen, die für den Aufbau von neuronalen Netzwerken verwendet  werden, einschließlich der Definition von Schichten, Verlustfunktionen ( siehe line 7)
import torch.optim as optim     # hier wird das Optimierungspackage von PyTorch importiert.Es enthält verschiedene Optimierungsalgorithmen, die beim Training neuronaler Netzwerke verwendet werden, wie Stochastic Gradient Descent und Adam ( siehe line 32)
import torch.nn.functional as F # Dies importiert das Modul functional aus PyTorch unter dem Namen F. Dieses Modul enthält Funktionen wie z.B. Aktivierungsfunktionen (ReLU, Sigmoid, usw.) und Verlustfunktionen (z.B.line 14)
import os                       # Hier wird noch os importiert, was gebraucht wird um die trainierten modelle zu speichern, respektiv ordner zu erstellen in welchen die Modelle gespeichert werden können(siehe line 18-24)
 
# Hier wird ein einfaches, zweischichtiges, lineares Neuronalesnetzwerk erstellt
class Linear_QNet(nn.Module):                              # Hier wird die Klasse Linear_QNet definiert, die von nn.Module erbt. Dies bedeutet, dass Linear_QNet eine Unterklasse von nn.Module ist und alle Funktionen und Eigenschaften von nn.Module erbt.
    def __init__(self, input_size, hidden_size, output_size):
        super().__init__()
        self.linear1 = nn.Linear(input_size, hidden_size)  # Hier wird die erste lineare Schicht (linear1) erstellt und initialisiert. nn.Linear(input_size, hidden_size) erstellt eine lineare Schicht mit input_size als Input featur und hidden_size als output feature.
        self.linear2 = nn.Linear(hidden_size, output_size) # Erstellung von einem zweiten linearen layer mit dem Input feature hidden_size (output vom ersten layer) und dem output featur output_size
 
    def forward(self, x):                                  # Hier wird die Methode forward definiert, die verwendet wird, um den Vorwärtsdurchlauf des neuronalen Netzwerks auszuführen. Es ist eine Funktion, die klärt wie die Daten von neuron zu euron geleitet werden , damit keine Fehler passieren. Der Parameter self ist eine Referenz auf die Instanz der Klasse selbst, während x die Eingabedaten sind, die durch das Netzwerk fließen.
        x = F.relu(self.linear1(x))
        x = self.linear2(x)                                # Nach der Anwendung der ReLU-Aktivierungsfunktion wird die Ausgabe durch die zweite lineare Schicht (self.linear2) geleitet. Dieser Schritt führt eine weitere lineare Transformation durch, ohne eine Aktivierungsfunktion anzuwenden. x wird wieder überschreiben, von den outputs des 2. layers.
        return x                                           # Zum Schluss wird die Ausgabe x zurückgegeben. Dies ist die Vorhersage oder Ausgabe des neuronalen Netzwerks nach dem Vorwärtsdurchlauf.
 
    # Speichern des trainierten Modelles in einem Ordner
 
    def save(self, file_name='model.pth'):                 # Diese Zeile definiert eine Methode namens save in der Klasse Linear_QNet. Die Methode hat einen Parameter file_name, der standardmäßig auf 'model.pth' gesetzt ist. Diese Methode wird verwendet, um das trainierte Modell zu speichern.
        model_folder_path = './model'                      # Hier wird der Pfad zum Ordner definiert, in dem das Modell gespeichert werden soll. Der Pfad wird als './model' festgelegt.
        if not os.path.exists(model_folder_path):          # Diese Zeile überprüft, ob der Ordner model im aktuellen Verzeichnis existiert. Die Bedingung not os.path.exists(model_folder_path) gibt True zurück, wenn der Ordner nicht existiert.
            os.makedirs(model_folder_path)                 # Wenn der Ordner nicht existiert, wird er mit os.makedirs() erstellt. Dadurch geht man sicher, dass das Modell im Ordner gespeichert werden kann.
 
        file_name = os.path.join(model_folder_path, file_name) # Hier wird der vollständige Dateipfad für das zu speichernde Modell erstellt, indem der Ordnerpfad (model_folder_path) und der Dateiname (file_name) kombiniert werden
        torch.save(self.state_dict(), file_name)               # Schließlich wird das Modell mithilfe der torch.save()-Funktion im Dateipfad file_name gespeichert. self.state_dict() gibt die Parameter des Modells zurück, die dann in der Datei gespeichert werden. Das trainierte Model ist also nun gespeichert.
 
 
#Training des Modelles
 
class QTrainer:                                                      # Diese Zeile definiert eine neue Klasse namens QTrainer, die für das Training des Modells verwendet wird.
    def __init__(self, model, lr, gamma):                            # __init__ Methode wird definiert( Konstruktor der Klasse). Jedes neu erstellte Objekt hat 3 Parameter: model ( das neuronalenetzwerk, welches trainiert werden soll), lr ( Die lernrate, die vom Optimierer angepasst wird, um die Gewichte zu aktualisieren ) und gamma(Diskontierungsfaktor)
        self.lr = lr
        self.gamma = gamma                                           # Ist wie die Balance von lang- und kurzzeit Gedächtnis. Der Diskontierungsfaktor bestimmt, wie stark zukünftige Belohnungen in der aktuellen Entscheidung berücksichtigt werden. Normalerweise wird ein Wert zwischen 0 und 1 verwendet, wobei 0 bedeutet, dass zukünftige Belohnungen nicht berücksichtigt werden (kurzsichtige Entscheidungen) und 1 bedeutet, dass zukünftige Belohnungen genauso wichtig sind wie sofortige Belohnungen (langfristige Entscheidungen).
        self.model = model                                          
        self.optimizer = optim.Adam(model.parameters(), lr=self.lr)  # Hier wird ein Adam-Optimierer (optim.Adam) erstellt, der verwendet wird, um die Gewichte des Modells während des Trainings zu optimieren. Die Gewichte/Parameter des Modells (model.parameters()) werden als Argument übergeben, und die Lernrate (lr) wird ebenfalls festgelegt.
        self.criterion = nn.MSELoss()                                # Hier wird der Mean Squared Error (MSE) Loss (nn.MSELoss()) erstellt, der verwendet wird, um den Fehler zwischen den Vorhersagen des Modells und den tatsächlichen Zielwerten zu berechnen. Diese Fehlerfunktion wird später im Trainingsprozess verwendet, um den Fehler zu minimieren und das Modell anzupassen.
 
    def train_step(self, state, action, reward, next_state, done):   # Diese Zeile definiert die Methode train_step, die zur Durchführung eines Trainingschritts für das Q-Learning-Modell verwendet wird. Die Methode hat fünf Parameter:
                                                                     # 1. state: Der Zustand, in dem sich das Modell befindet.
                                                                     # 2. action: Die Aktion, die das Modell ausführt.
                                                                     # 3. reward: Die Belohnung, die das Modell für die ausgeführte Aktion erhält.
                                                                     # 4. next_state: Der nächste Zustand, den das Modell nach Ausführung der Aktion einnimmt.
                                                                     # 5. done: Eine Flagge, die angibt, ob der Trainingsprozess abgeschlossen ist.
        state = torch.tensor(state, dtype=torch.float)               # Hier werden die übergebenen Zustandsdaten in einen Tensor konvertiert. Der torch.tensor()-Aufruf erstellt einen Tensor aus den Zustandsdaten und setzt den Datentyp auf torch.float
        next_state = torch.tensor(next_state, dtype=torch.float)     # Ähnlich wie in line 46 werden die übergebenen Daten des nächsten Zustands in einen Tensor konvertiert, wobei der Datentyp auf torch.float gesetzt wird.
        action = torch.tensor(action, dtype=torch.long)              # Hier werden die übergebenen Aktionsdaten in einen Tensor konvertiert. Der Datentyp wird auf torch.long gesetzt, da es sich um diskrete Aktionen handelt, die als Ganzzahlen dargestellt werden.
        reward = torch.tensor(reward, dtype=torch.float)             # Die übergebenen Belohnungsdaten werden in einen Tensor konvertiert, wobei der Datentyp auf torch.float gesetzt wird.
        # (n, x)

        if len(state.shape) == 1: # Die Bedingung if len(state.shape) == 1: überprüft, ob der Zustand ein eindimensionaler Tensor ist. 
                                  # Ein eindimensionaler Tensor hätte eine Form wie [n], wobei 'n' die Anzahl der Elemente im Tensor ist.
                                  
            state = torch.unsqueeze(state, 0) # Wenn der Zustand ein eindimensionaler Tensor ist, wird er in einen zweidimensionalen Tensor umgeformt, 
                                              # indem eine zusätzliche Dimension hinzugefügt wird. 
                                              # Dies geschieht mit der Funktion torch.unsqueeze.
                                              # Dies wird mit state, next_state, action und reward gemacht
            next_state = torch.unsqueeze(next_state, 0) 
            action = torch.unsqueeze(action, 0)
            reward = torch.unsqueeze(reward, 0)
            done = (done, ) # Da es sich bei done um einen einzelnen wert handelt wird dort das gleiche gemacht einfach nur manuell 

    
        pred = self.model(state) # Hier wird der Q-Werte berechnet für den aktuellen Zustand (state) mithilfe des Q-Netzwerks self.model.

        target = pred.clone() #Hier wird eine  Kopie der Vorhersage (pred) erstellt. Die Verwendung von clone() stellt sicher, dass Änderungen an target die Vorhersage pred nicht beeinflussen.
        for idx in range(len(done)): # Nun werden die Ziel-Q-Werte für jeden Übergang aktualisiert. Die Variable idx wird verwendet, um die Elemente in done, reward usw. zu durchlaufen.
            Q_new = reward[idx] #Für jede durchführung der Schleife wird zuerst der aktuelle Q-Wert (Q_new) initialisiert.
            
            if not done[idx]: #Solange die Schleife nicht abgeschlossen ist:
                Q_new = reward[idx] + self.gamma * torch.max(self.model(next_state[idx]))  #Wird der neue Q-Wert (Q_new) mit der Bellman-Gleichung berechnet
 
            target[idx][torch.argmax(action[idx]).item()] = Q_new # Schlissloch wird der eintrag in target aktualisiert um den neuen Q_Wert zu erhalten
    

        self.optimizer.zero_grad()  # Dieser Befehl setzt die Gradienten aller Parameter im Netzwerk auf Null. Dies ist wichtig, da PyTorch die Gradienten akkumuliert, wenn backward() aufgerufen wird, und wir sicherstellen möchten, dass sie für jede Iteration des Trainings zurückgesetzt werden.
        loss = self.criterion(target, pred) #Hier wird der Verlust berechnet. Die Variable loss enthält den Wert der Verlustfunktion, die zwischen den vorhergesagten Q-Werten (pred) und den Ziel-Q-Werten (target) berechnet wurde. Die Verlustfunktion wurde zuvor in der Initialisierung des QTrainer-Objekts festgelegt.
        loss.backward() # Mit diesem Befehl werden die Gradienten der Verlustfunktion bezüglich der Netzwerkparameter berechnet. Dies ist der Backpropagation-Schritt, bei dem die Gradienten durch das Netzwerk propagiert werden, um zu bestimmen, wie jeder Parameter angepasst werden muss, um den Verlust zu minimieren.

        self.optimizer.step() #Schließlich führt dieser Befehl einen Optimierungsschritt aus, bei dem die Parameter des Netzwerks mithilfe der berechneten Gradienten und des von Ihnen gewählten Optimierungsalgorithmus aktualisiert werden. Der Optimierungsschritt basiert auf den berechneten Gradienten und dem Lernraten- und Optimierungsalgorithmus, der in der Initialisierung des QTrainer-Objekts festgelegt wurde.


