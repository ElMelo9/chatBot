from PyQt6.QtWidgets import QApplication, QDialog,QMessageBox
from view.formulario1 import Formulario1
from view.formulario2 import Formulario2
from models.crudMySql  import MySQL
from controller.chatBoot import Bot
import sys
import re

#instancias
chatBot=Bot()
db=MySQL()

class MyDialog1(QDialog, Formulario1):
    validador = False
    id=0
    nombre=""

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Conecta eventos a funciones de manejo
        self.Btnenviar.clicked.connect(self.enviar_clicked)
        self.BtnSalir.clicked.connect(self.salir_clicked)

    def enviar_clicked(self):
        email = self.TxtEmail.text()
        tipo_documento = (self.CmbTipodoc.currentIndex()+1)
        numero_documento = self.TxtNumdoc.text()
        nombre = self.TxtNombre.text()
        telefono = self.TxtTel.text()

        # Validadores de datos
        if not numero_documento.isdigit():
            if not numero_documento.strip():
                self.TxtNumdoc.setText("Por favor ingrese un Documento")
                self.TxtNumdoc.setStyleSheet("border-radius:10px;color: red;")
            else:
                self.TxtNumdoc.setText("Por favor ingrese un Documento valido")
                self.TxtNumdoc.setStyleSheet("border-radius:10px;color: red;")
        elif not nombre.strip():
            self.TxtNombre.setText("Por favor ingrese un nombre.")
            self.TxtNombre.setStyleSheet("border-radius:10px;color: red;")
        elif not email_valido(email):
            if not email.strip():
                self.TxtEmail.setText("Por favor ingrese un Email")
                self.TxtEmail.setStyleSheet("border-radius:10px;color: red;")
            else:
                self.TxtEmail.setStyleSheet("border-radius:10px;color: red;")
        elif not telefono.isdigit():
            if not telefono.strip():
                self.TxtTel.setText("Por favor ingrese un Telefono")
                self.TxtTel.setStyleSheet("border-radius:10px;color: red;")
            else:
                self.TxtTel.setText("Por favor ingrese un valido")
                self.TxtTel.setStyleSheet("border-radius:10px;color: red;")
        else:        

            #preparmamos una data con el insert
            data = {
                'id_tipoDoc': tipo_documento, 
                'doc_usuario': numero_documento,  
                'nombre_usuario': nombre,
                'email_usuario': email,
                'telefono_usuario': telefono 
            }

            #insertamos la data en la bd
            db.insert_usuario(data)

            # Abre el segundo formulario de manera no modal
            self.abrir_formulario2(nombre)
            self.validador = True
            self.close()

    def abrir_formulario2(self,nombre):
        self.id=db.get_id_usuario(nombre)
        self.nombre=nombre
        dialog2 = MyDialog2()
        dialog2.getIdUser(self.id,self.nombre)
        dialog2.show()

    def salir_clicked(self):
        self.close()


class MyDialog2(QDialog, Formulario2):
    id_usuario=0
    nombre_usuario=""
    conversation_history = []

    def __init__(self):
        super().__init__()
        self.setupUi(self)


        # Conecta eventos a funciones de manejo
        self.Btnenviarp.clicked.connect(self.enviar_clicked)
        self.BtnConsultar.clicked.connect(self.consultar_clicked)
        self.tabWidget.currentChanged.connect(self.tab_changed) 

    def getIdUser(self,id_usuario,nombre_usuario):
            self.id_usuario=id_usuario
            self.nombre_usuario=nombre_usuario

    def tab_changed(self, index):
        if index == 0:
            self.CmbFechah.clear()
            self.CmbNombre.clear()
        elif index == 1:
            fechas=db.get_fechasHistorial()
            usuarios=db.get_usuariosHistorial()
            for fecha in fechas:
                self.CmbFechah.addItem(str(fecha))
            for usuario in usuarios:
                self.CmbNombre.addItem(str(usuario))    

    def enviar_clicked(self):
        textCliente=self.TxtPregunta.text()
        self.TxtChatb.setText(self.TxtChatb.toPlainText()+'\n🧑 '+self.nombre_usuario+': '+ textCliente+'\n----------')
        self.conversation_history.append('\n🧑 '+self.nombre_usuario+': '+ textCliente+'\n----------')
        self.TxtPregunta.setText('')
        # Bucle principal del chatbot
        while True:

            if textCliente.lower() in ['bye', 'goodbye','adios']:
                self.TxtChatb.setText(self.TxtChatb.toPlainText()+'\n🤖Dende: ¡Hasta luego!'+'\n----------')
                print('Chatbot: ¡Hasta luego!')
            break

        # Generar respuesta del chatbot
        chatbot_response = chatBot.generate_response(textCliente)

        # Imprimir la respuesta del chatbot
        self.TxtChatb.setText(self.TxtChatb.toPlainText()+'\n🤖Dende: '+ chatbot_response+'\n----------')
        self.conversation_history.append('\n🤖Dende: '+ chatbot_response+'\n----------')
    
    def consultar_clicked(self):
        historialChats=db.get_historialChat(self.CmbNombre.currentText(),self.CmbFechah.currentText())

        for chat in historialChats:
            self.TxtHistorial.setText(self.TxtHistorial.toPlainText()+chat+"\n")

    def salir_clicked(self):
        self.close()       

    def closeEvent(self, event):

        confirmar_cierre = QMessageBox.question(self, "Confirmar Cierre", "¿Estás seguro de que quieres cerrar el formulario?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if confirmar_cierre == QMessageBox.StandardButton.Yes:
            # Obtener el texto del QTextBrowser
            text = self.TxtChatb.toPlainText()
            if not (text.strip() == ""):
                # Ejecuta tu acción aquí antes de cerrar el formulario
                db.insert_historial_chat(self.id_usuario,limpiar_mensajes(self.conversation_history))
                 
            event.accept()  # Acepta el cierre del formulario
        else:
            event.ignore()  # Ignora el cierre del formulario




def email_valido(email):
    # Patrón de expresión regular para validar una dirección de correo electrónico
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    # Utiliza re.match() para verificar si el email coincide con el patrón
    if re.match(patron, email):
        return True
    else:
        return False

def limpiar_mensajes(conversation_history):
    mensajes_limpios = []
    for mensaje in conversation_history:
        # Eliminar iconos y "\n" utilizando expresiones regulares
        mensaje_limpio = re.sub(r'[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F700-\U0001F77F\U0001F780-\U0001F7FF\U0001F800-\U0001F8FF\U0001F900-\U0001F9FF\U0001FA00-\U0001FA6F\U0001FA70-\U0001FAFF\U0001FB00-\U0001FBFF\U0001FC00-\U0001FCFF\U0001FD00-\U0001FDFF\U0001FE00-\U0001FEFF\U0001FF00-\U0001FFFF\U00020000-\U0002A6DF\U0002A700-\U0002B73F\U0002B740-\U0002B81F\U0002B820-\U0002CEAF\U0002CEB0-\U0002EBEF\U0002F800-\U0002FA1F\n]', '', mensaje)
        # Eliminar caracteres de nueva línea "\n"
        mensaje_limpio = mensaje_limpio.replace('\n', ' ')
        mensajes_limpios.append(mensaje_limpio.strip())  # Eliminar espacios en blanco al principio y al final
    return mensajes_limpios

#### Desca aca comienza el Programa####
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = MyDialog1()
    dialog.show()

    while not dialog.validador: # Mientras el validador sea False
        app.processEvents()     # Procesar eventos de la aplicación para mantenerla receptiva

    dialog2 = MyDialog2()
    dialog2.getIdUser(dialog.id,dialog.nombre)
    dialog2.show()

    sys.exit(app.exec())