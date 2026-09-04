import tkinter as tk
from tkinter import ttk, messagebox
import dolar_api

# Creamos una instancia de la clase DollarExchangeTypes
dolar_exchange_types = dolar_api.DollarExchangeTypes()


# Funcion del evento
def dolar_update_info():
    # LLamamos al metodo call para traer la api
    dolar_exchange_types.call()

    if dolar_exchange_types.status_message is not None:
        # Si ocurre una excpecion mostramos el status
        label_oficial.config(text=dolar_exchange_types.status_message)
        label_blue.config(text=dolar_exchange_types.status_message)
        label_bcra.config(text=dolar_exchange_types.status_message)
        label_bolsa.config(text=dolar_exchange_types.status_message)

        # Mostramos un mensaje de error
        messagebox.showerror("Actulización no completada", "No se puedo actulizar la información")

    else:
        # Si la llamada es exitosa, llamamos a los metodos de cada tipo de dolar y actualizamos
        dolar_exchange_types.dollar_oficial()
        label_oficial.config(text=f'Dolar Oficial\n'
                                  f'Compra: {dolar_exchange_types.info_buy()}\n'
                                  f'Venta: {dolar_exchange_types.info_sell()}')

        dolar_exchange_types.dollar_blue()
        label_blue.config(text=f'Dolar Blue\n'
                               f'Compra: {dolar_exchange_types.info_buy()}\n'
                               f'Venta: {dolar_exchange_types.info_sell()}')
        
        dolar_exchange_types.dollar_bolsa()
        label_bolsa.config(text=f'Dolar Bolsa\n'
                               f'Compra: {dolar_exchange_types.info_buy()}\n'
                               f'Venta: {dolar_exchange_types.info_sell()}')
        
        dolar_exchange_types.dollar_mayorista()
        label_mayorista.config(text=f'Dolar Mayorista\n'
                                    f'Compra: {dolar_exchange_types.info_buy()}\n'
                                    f'Venta: {dolar_exchange_types.info_sell()}')

        # Mostramos un mensaje de exito
        messagebox.showinfo("Actualización completada", "La información del dólar ha sido actualizada correctamente.")


# Creamos la ventana y le damos caracteristicas
main_window = tk.Tk()
main_window.geometry('700x400')
main_window.title('Dolar APP')
main_window.config(background='gray')

# Creamos una etiqueta de titulo
label_title = ttk.Label(main_window,
                        text="Cotización del dolar en tiempo real",
                        font=("Helvetica", 14),
                        foreground='black',
                        background='gray62',
                        wraplength=300,
                        justify='center')
label_title.grid(column=1, row=0, columnspan=2, sticky='NS')

# Configurar el grid
main_window.rowconfigure(1, weight=2)
main_window.columnconfigure(0, weight=2)
main_window.columnconfigure(1, weight=2)
main_window.columnconfigure(2, weight=2)
main_window.columnconfigure(3, weight=2)

# Creamos las etiquetas para los tipos de cambio

# label para el dolar oficial
label_oficial = ttk.Label(main_window,
                          text=f'Dolar Oficial\n'
                               f'Compra: ---,---\n'
                               f'Venta: ---,---',
                          font=("Helvetica", 14),
                          foreground='black',
                          background='gray62',
                          wraplength=200,
                          justify='center')
label_oficial.grid(column=0, row=1)

# label para el dolar blue
label_blue = ttk.Label(main_window,
                       text=f'Dolar Blue\n'
                            f'Compra: ---,---\n'
                            f'Venta: ---,---',
                       font=("Helvetica", 14),
                       foreground='black',
                       background='gray62',
                       wraplength=200,
                       justify='center')
label_blue.grid(column=1, row=1)

# label para el dolar bolsa
label_bolsa = ttk.Label(main_window,
                       text=f'Dolar Bolsa\n'
                            f'Compra: ---,---\n'
                            f'Venta: ---,---',
                       font=("Helvetica", 14),
                       foreground='black',
                       background='gray62',
                       wraplength=200,
                       justify='center')
label_bolsa.grid(column=2, row=1)

# label para el dolar mayorista
label_mayorista = ttk.Label(main_window,
                            text=f'Dolar Mayorista\n'
                                 f'Compra: ---,---\n'
                                 f'Venta: ---,---',
                            font=("Helvetica", 14),
                            foreground='black',
                            background='gray62',
                            wraplength=200,
                            justify='center')
label_mayorista.grid(column=3, row=1)

# Definimos el botón para actualizar la cotización

refresh_button = ttk.Button(main_window, text='Actualizar', command=dolar_update_info)
refresh_button.grid(row=2, column=1, columnspan=2, sticky='NSWE', padx=20, pady=50)

# Le damos estilo al botón
button_style = ttk.Style()
button_style.theme_use('alt')
button_style.configure('TButton',
                       font=('Helvetica', 12),
                       foreground='black',
                       background='gray',
                       width=20,
                       focuscolor='none')

# Iniciamos la ventana hasta que se cierra el programa
main_window.mainloop()
