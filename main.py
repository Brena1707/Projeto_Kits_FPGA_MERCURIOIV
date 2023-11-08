from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from PIL import ImageTk, Image
from datetime import datetime
import json
import arquivo

window = Tk()
window.title("Gerador de Código")

window.geometry("730x480")
window.configure(bg="#FFFFFF")


nome_do_projeto = StringVar()
prefixo = StringVar()

check_vhdl = BooleanVar()
check_v = BooleanVar()
check_clock = BooleanVar()
check_PROTO_A = BooleanVar()
check_PROTO_B = BooleanVar()
check_segmentos = BooleanVar()
check_chave = BooleanVar()
check_LED_MATRIX = BooleanVar()
check_button = BooleanVar()
check_VGA = BooleanVar()
check_GPIO = BooleanVar()
check_LCD = BooleanVar()
check_Ethernet = BooleanVar()
check_I2C = BooleanVar()
check_RS232 = BooleanVar()
check_SD_CARD = BooleanVar()
check_SDRAM = BooleanVar()
check_PMOD = BooleanVar()
check_flash = BooleanVar()
check_LED_RGB = BooleanVar()
check_ADC = BooleanVar()
check_DAC = BooleanVar()
check_SA_SB = BooleanVar()
check_ext_clock = BooleanVar()
check_SW = BooleanVar()
check_USB = BooleanVar()
check_UART = BooleanVar()
check_ConnectGPIO = BooleanVar()

def get_diretorio_arquivos():
    diretorio = askdirectory()
    print(diretorio)
    return diretorio


def get_prefixo():
    print(prefixo.get())


def get_arquivo(tipo):
    tipo_do_arquivo = (('text files', tipo), ('All files', '*.*'))
    nome_do_arquivo = fd.askopenfilename(title='Open a file', initialdir='/', filetypes=tipo_do_arquivo)

    return nome_do_arquivo


def gerar_caixa_de_dialogo(titulo, mensagem):
    showinfo(title=titulo, message=mensagem)


def get_nome_do_projeto():
    return nome_do_projeto.get().upper()


def gerar_arquivo_qpf(diretorio=''):
    projeto = get_nome_do_projeto()
    nome_arquivo = '{}.qpf'.format(projeto)
    nome_arquivo = diretorio + '/' + nome_arquivo
    data = datetime.now()

    qpf = open(nome_arquivo, 'w')
    qpf.write(data.strftime('DATE = \"%H:%M:%S %B %d, %Y\"\n'))
    qpf.write('QUARTUS_VERSION = \"16.0.0\"\n')
    qpf.write('\n')
    qpf.write('# Revisions\n')
    qpf.write('\n')
    qpf.write('PROJECT_REVISION = \"{}\"\n'.format(get_nome_do_projeto()))

    qpf.close()


def gerar_arquivo_qsf(diretorio=''):
    projeto = get_nome_do_projeto()
    nome_arquivo = '{}.qsf'.format(projeto)
    nome_arquivo = diretorio + '/' + nome_arquivo
    data = datetime.now()

    if check_clock.get():
        f = open('auxiliar/qsf/CLOCK.aux', 'r')
        clock_buffer = f.read()
        f.close()

    if check_ext_clock.get():
        f = open('auxiliar/qsf/EXT_CLOCK.aux', 'r')
        ext_clock_buffer = f.read()
        f.close()

    if check_chave.get():
        f = open('auxiliar/qsf/SW.aux', 'r')
        chave_buffer = f.read()
        f.close()

    if check_button.get():  #KEY
        f = open('auxiliar/qsf/KEY.aux', 'r')
        button_buffer = f.read()
        f.close()

    if check_segmentos.get():
        f = open('auxiliar/qsf/DISPLAY.aux', 'r')
        segmentos_buffer = f.read()
        f.close()

    if check_LED_MATRIX.get():
        f = open('auxiliar/qsf/LED_MX.aux', 'r')
        led_buffer = f.read()
        f.close()

    if check_LED_RGB.get():
        f = open('auxiliar/qsf/LED_RGB.aux', 'r')
        led_rgb_buffer = f.read()
        f.close()

    if check_I2C.get():
        f = open('auxiliar/qsf/TEMP_SENS.aux', 'r')
        i2c_buffer = f.read()
        f.close()

    if check_LCD.get():
        f = open('auxiliar/qsf/LCD.aux', 'r')
        lcd_buffer = f.read()
        f.close()

    if check_VGA.get():
        f = open('auxiliar/qsf/VGA.aux', 'r')
        vga_buffer = f.read()
        f.close()
    # if check_UART.get():
    #     pass

    # if check_USB.get():
    #     pass

    if check_ADC.get():
        f = open('auxiliar/qsf/ADC.aux', 'r')
        adc_buffer = f.read()
        f.close()

    if check_DAC.get():
        f = open('auxiliar/qsf/DAC.aux', 'r')
        dac_buffer = f.read()
        f.close()

    if check_SD_CARD.get():
        f = open('auxiliar/qsf/SD_CARD.aux', 'r')
        micro_sd_buffer = f.read()
        f.close()

    if check_SDRAM.get():
        f = open('auxiliar/qsf/SDRAM.aux', 'r')
        sdram_64_buffer = f.read()
        f.close()

    if check_Ethernet.get():
        f = open('auxiliar/qsf/ETHERNET.aux', 'r')
        ethernet_buffer = f.read()
        f.close()

    if check_PMOD.get():
        f = open('auxiliar/qsf/PMOD.aux', 'r')
        pmod_buffer = f.read()
        f.close()

    if check_GPIO.get():
        f = open('auxiliar/qsf/GPIO.aux', 'r')
        gpio_buffer = f.read()
        f.close()

    if check_SA_SB.get():
        f = open('auxiliar/qsf/EXPANSION_KEY.aux', 'r')
        sa_sb_buffer = f.read()
        f.close()

    if check_SW.get():
        f = open('auxiliar/qsf/SW.aux', 'r') ##MUDAR AQUI
        SW_buffer = f.read()
        f.close()

    if  check_ConnectGPIO.get():
        f = open('auxiliar/qsf/GPIO.aux', 'r') ##MUDAR AQUI
        check_connectGPIO_buffer = f.read()
        f.close()

    with open(nome_arquivo, 'w') as qsf:

        if check_vhdl.get():
            qsf.write('#============================================================\n'
                    '# Build by Terasic System Builder\n'
                    '#============================================================\n\n')
            qsf.write('set_global_assignment -name FAMILY "Cyclone IV E"\n')
            qsf.write('set_global_assignment -name DEVICE EP4CE30F23C7\n')
            qsf.write('set_global_assignment -name TOP_LEVEL_ENTITY "{}"\n'.format(projeto))
            qsf.write('set_global_assignment -name ORIGINAL_QUARTUS_VERSION "13.0 SP1"\n')
            qsf.write('set_global_assignment -name LAST_QUARTUS_VERSION "18.1.0 Lite Edition"\n')
            qsf.write('set_global_assignment -name PROJECT_CREATION_TIME_DATE "{}"\n'.format(data.strftime('%H:%M:%S %B %d,%Y')))
            qsf.write('set_global_assignment -name PROJECT_OUTPUT_DIRECTORY output_files\n')
            qsf.write('set_global_assignment -name MIN_CORE_JUNCTION_TEMP 0\n')
            qsf.write('set_global_assignment -name MAX_CORE_JUNCTION_TEMP 85\n')
            qsf.write('set_global_assignment -name ERROR_CHECK_FREQUENCY_DIVISOR 1\n')
            qsf.write('set_global_assignment -name NOMINAL_CORE_SUPPLY_VOLTAGE 1.2V\n')
            qsf.write('set_global_assignment -name EDA_SIMULATION_TOOL "ModelSim-Altera (VHDL)"\n')
            qsf.write('set_global_assignment -name EDA_OUTPUT_DATA_FORMAT VHDL -section_id eda_simulation\n')

            qsf.write('set_global_assignment -name VHDL_FILE ../src/{}.vhd\n'.format(projeto))
            qsf.write('set_global_assignment -name SDC_FILE {}.sdc\n\n'.format(projeto))

            #qsf.write('set_global_assignment -name SDC_FILE {}.SDC\n'.format(projeto))

        if check_v.get():
            qsf.write('#============================================================\n'
            '# Build by Terasic System Builder\n'
            '#============================================================\n\n')
            qsf.write('set_global_assignment -name FAMILY "Cyclone IV E"\n')
            qsf.write('set_global_assignment -name DEVICE EP4CE30F23C7\n')
            qsf.write('set_global_assignment -name TOP_LEVEL_ENTITY "{}"\n'.format(projeto))
            qsf.write('set_global_assignment -name ORIGINAL_QUARTUS_VERSION "13.0 SP1"\n')
            qsf.write('set_global_assignment -name LAST_QUARTUS_VERSION "18.1.0 Lite Edition"\n')
            qsf.write('set_global_assignment -name PROJECT_CREATION_TIME_DATE "{}"\n'.format(data.strftime('%H:%M:%S %B %d,%Y')))
            qsf.write('set_global_assignment -name PROJECT_OUTPUT_DIRECTORY output_files\n')
            qsf.write('set_global_assignment -name MIN_CORE_JUNCTION_TEMP 0\n')
            qsf.write('set_global_assignment -name MAX_CORE_JUNCTION_TEMP 85\n')
            qsf.write('set_global_assignment -name ERROR_CHECK_FREQUENCY_DIVISOR 1\n')
            qsf.write('set_global_assignment -name NOMINAL_CORE_SUPPLY_VOLTAGE 1.2V\n')
            qsf.write('set_global_assignment -name EDA_SIMULATION_TOOL "ModelSim-Altera (VHDL)"\n')
            qsf.write('set_global_assignment -name EDA_OUTPUT_DATA_FORMAT VHDL -section_id eda_simulation\n')

            qsf.write('set_global_assignment -name verilog_FILE ../src/{}.vhd\n'.format(projeto))
            qsf.write('set_global_assignment -name SDC_FILE {}.sdc\n\n'.format(projeto))

                #qsf.write('set_global_assignment -name SDC_FILE {}.SDC\n'.format(projeto))

        if check_clock.get():
            qsf.write(clock_buffer)
            qsf.write('\n')

        if check_ext_clock.get():
            qsf.write(ext_clock_buffer)
            qsf.write('\n')

        if check_chave.get():
            qsf.write(chave_buffer)
            qsf.write('\n')

        if check_button.get(): #KEY
            qsf.write(button_buffer)
            qsf.write('\n')

        if check_segmentos.get():
            qsf.write(segmentos_buffer)
            qsf.write('\n')

        if check_LED_MATRIX.get():
            qsf.write(led_buffer)
            qsf.write('\n')

        if check_LED_RGB.get():
            qsf.write(led_rgb_buffer)
            qsf.write('\n')

        if check_I2C.get():
            qsf.write(i2c_buffer)
            qsf.write('\n')

        if check_LCD.get():
            qsf.write(lcd_buffer)
            qsf.write('\n')

        if check_VGA.get():
            qsf.write(vga_buffer)
            qsf.write('\n')

        # if check_UART.get():
        #     pass

        # if check_USB.get():
        #     pass

        if check_ADC.get():
            qsf.write(adc_buffer)
            qsf.write('\n')

        if check_DAC.get():
            qsf.write(dac_buffer)
            qsf.write('\n')

        if check_SD_CARD.get():
            qsf.write(micro_sd_buffer)
            qsf.write('\n')

        if check_SDRAM.get():
            qsf.write(sdram_64_buffer)
            qsf.write('\n')

        if check_Ethernet.get():
            qsf.write(ethernet_buffer)
            qsf.write('\n')

        if check_PMOD.get():
            qsf.write(pmod_buffer)
            qsf.write('\n')

        if check_GPIO.get():
            qsf.write(gpio_buffer)
            qsf.write('\n')

        if check_SW.get():
            qsf.write(SW_buffer)
            qsf.write('\n')

        if check_SA_SB.get():
            qsf.write(sa_sb_buffer)
            qsf.write('\n')

        if check_ConnectGPIO.get():
            qsf.write(check_connectGPIO_buffer)
            qsf.write('\n')


def criar_selecao(label, varialvel, coluna, posicao):
    espacamento = 13

    if coluna == 1:
        Checkbutton(frame_selecao, text=label, onvalue=True, offvalue=False, variable=varialvel).place(relx=0.05, rely=posicao/espacamento)
    elif coluna == 2:
        Checkbutton(frame_selecao, text=label, onvalue=True, offvalue=False, variable=varialvel).place(relx=0.6, rely=posicao/espacamento)
    else:
        print('Só há duas colunas')


def gerar_arquivo_v(diretorio=''):
    projeto = get_nome_do_projeto()
    nome_arquivo = '{}.v'.format(projeto)
    nome_arquivo = diretorio + '/' + nome_arquivo

    
    v = open(nome_arquivo, 'w')
    v.write('//=======================================================\n')
    v.write('// This code is generated by Brena Marques\n')
    v.write('//=======================================================\n')
    v.write('module {}(\n'.format(projeto))

    if check_clock.get():
        v.write('\t//////////// CLOCK ////////////\n')
        v.write("input\t\t\t\tCLOCK_50MHz,\n")
        v.write("input\t\t\t\tCLOCK1_50MHz,\n\n")

    if check_ext_clock.get():
        v.write("//////////// EXT_CLK //////////\n")
        v.write("input\t\t\t\tSMA_CLKIN,\n")
        v.write("input\t[1:0]\t\tGPIO0_CLKIN,\n")
        v.write("input\t[1:0]\t\tGPIO1_CLKIN,\n")
        v.write("output\t\t\t\tSMA_CLKOUT,\n")
        v.write("output\t[1:0]\t\tGPIO0_CLKOUT,\n")
        v.write("output\t[1:0]\t\tGPIO1_CLKOUT,\n\n")

    if check_SW.get():
        v.write("//////////// SW //////////\n")
        v.write("input\t[3:0]\tSW,\n\n")
   
    if check_SW.get():
        v.write("//////////// SW //////////\n")
        v.write("input\t[3:0]\tSW,\n\n")

    if check_chave.get():
        v.write("//////////// KEY //////////\n")
        v.write("input\t[11:0]\tKEY,\n\n")

    if check_LED_RGB.get():
        v.write("//////////// LED_RGB //////////\n")
        v.write("output\t\t\t\tLED_R,\n")
        v.write("output\t\t\t\tLED_G,\n")
        v.write("output\t\t\t\tLED_B,\n\n")

    if check_segmentos.get():
        v.write("//////////// SEG7 //////////\n")
        v.write("output\t[7:0]\tDISP0_D,\n")
        v.write("output\t[7:0]\tDISP1_D,\n\n")

    if check_LED_MATRIX.get():
        v.write("//////////// LED_MATRIX //////////\n")
        v.write("output\t[4:0]\tLEDM_C,\n")
        v.write("output\t[7:0]\tLEDM_R,\n\n")

    if check_LCD.get():
        v.write("//////////// LCD //////////\n")
        v.write("inout\t[7:0]\tLCD_D,\n")
        v.write("output\t\t\t\tLCD_RS,\n")
        v.write("output\t\t\t\tLCD_RW,\n")
        v.write("output\t\t\t\tLCD_EN,\n")
        v.write("output\t\t\t\tLCD_BACKLIGHT,\n\n")

    if check_UART.get():
        v.write("//////////// UART //////////\n")
        v.write("output\t\t\t\tUART_TXD,\n")
        v.write("input\t\t\t\tUART_RXD,\n")
        v.write("input\t\t\t\tUART_CTS,\n")
        v.write("output\t\t\t\tUART_RTS,\n\n")

    if check_VGA.get():
        v.write("//////////// VGA //////////\n")
        v.write("output\t[3:0]\tVGA_R,\n")
        v.write("output\t[3:0]\tVGA_G,\n")
        v.write("output\t[3:0]\tVGA_B,\n")
        v.write("output\t\t\t\tVGA_HS,\n")
        v.write("output\t\t\t\tVGA_VS,\n\n")

    if check_SDRAM.get():
        v.write("//////////// SDRAM //////////\n")
        v.write("output\t[12:0]\tDRAM_A,\n")
        v.write("output\t[1:0]\tDRAM_BA,\n")
        v.write("output\t\t\t\tDRAM_CAS_N,\n")
        v.write("output\t\t\t\tDRAM_CKE,\n")
        v.write("output\t\t\t\tDRAM_CLK,\n")
        v.write("output\t\t\t\tDRAM_CS_N,\n")
        v.write("inout\t[15:0]\tDRAM_D,\n")
        v.write("output\t\t\t\tDRAM_RAS_N,\n")
        v.write("output\t[1:0]\tDRAM_DQM,\n")
        v.write("output\t\t\t\tDRAM_WE_N,\n\n")

    if check_USB.get():
        v.write("//////////// USB //////////\n")
        v.write("output\t\t\t\tUSB_WR,\n")
        v.write("output\t\t\t\tUSB_RD,\n")
        v.write("inout\t[7:0]\tUSB_D,\n")
        v.write("input\t\t\t\tUSB_POWEREN_N,\n")
        v.write("input\t\t\t\tUSB_RXF_N,\n")
        v.write("input\t\t\t\tUSB_TXE_N,\n\n")

    if check_SD_CARD.get():
        v.write("//////////// SD_CARD //////////\n")
        v.write("output\t\t\t\tSD_CMD,\n")
        v.write("output\t\t\t\tSD_CLK,\n")
        v.write("output\t\t\t\tSD_CD_N,\n")
        v.write("inout\t[3:0]\tSD_D,\n\n")

    if check_I2C.get():
        v.write("//////////// I2C //////////\n")
        v.write("inout\t\t\t\tI2C_SDA,\n")
        v.write("output\t\t\t\tI2C_SCL,\n")
        v.write("input\t\t\t\tI2C_OVERTEMP_N, //?\n\n")

    if check_Ethernet.get():
        v.write("//////////// ETHERNET //////////\n")
        v.write("output\t\t\t\tETH_TXEN,\n")
        v.write("output\t\t\t\tETH_TXEN,\n")
        v.write("output\t[3:0]\tETH_TXD,\n")
        v.write("input\t\t\t\tETH_RXER,\n")
        v.write("input\t\t\t\tETH_RXDV,\n")
        v.write("input\t[3:0]\tETH_RXD,\n")
        v.write("inout\t\t\t\tETH_MDIO,\n")
        v.write("output\t\t\t\tETH_MDC,\n")
        v.write("input\t\t\t\tETH_CRS,\n")
        v.write("input\t\t\t\tETH_COL,\n")
        v.write("output\t\t\t\tETH_RST_N,\n")
        v.write("input\t\t\t\tETH_RXCLK,\n")
        v.write("input\t\t\t\tETH_TXCLK,\n")
        v.write("output\t\t\t\tETH_TXER,\n\n")

    if check_ADC.get():
        v.write("//////////// ADC //////////\n")
        v.write("output\t\t\t\tADC_CNVST,\n")
        v.write("output\t\t\t\tADC_CS_N,\n")
        v.write("input\t\t\t\tADC_DOUT1,\n")
        v.write("input\t\t\t\tADC_DOUT2,\n")
        v.write("output\t\t\t\tADC_REFSEL,\n")
        v.write("output\t\t\t\tADC_SCLK,\n")
        v.write("output\t\t\t\tADC_SD,\n")
        v.write("output\t\t\t\tADC_SEL,\n")
        v.write("output\t\t\t\tADC_UB,\n\n")

    if check_DAC.get():
        v.write("//////////// DAC //////////\n")
        v.write("output\t\t\t\tDAC_CLR,\n")
        v.write("output\t\t\t\tDAC_CS_N,\n")
        v.write("output\t\t\t\tDAC_DIN,\n")
        v.write("output\t\t\t\tDAC_SCLK,\n\n")

    if check_flash.get():
        v.write("//////////// FLASH //////////\n")
        v.write("output\t\t\t\tFLASH_ASDO,\n")
        v.write("output\t\t\t\tFLASH_CS0_N,\n")
        v.write("inout\t\t\t\tFLASH_DATA0,	//?\n")
        v.write("output\t\t\t\tFLASH_DCLK,\n\n")

    if check_PROTO_A.get():
        v.write("//////////// PROTO_A //////////\n")
        v.write("inout\t[7:0]\tPROTO_A,\n\n")

    if check_PROTO_B.get():   
        v.write("//////////// PROTO_B //////////\n")
        v.write("inout\t[7:0]\tPROTO_B,\n\n")

    if check_GPIO.get():
        v.write("//////////// GPIO, GPIO connect SA-SB //////////\n")
        v.write("input\t[7:0]\tSA,\n")
        v.write("input\t[7:0]\tSB\n")


    if check_ConnectGPIO.get():
        v.write("//////////// GPIO, GPIO connect GPIO Default //////////\n")
        v.write("inout\t[35:0]\tGPIO_D,\n\n")

    v.write(');\n')
    v.write('\n')
    v.write('//=======================================================\n//  REG/WIRE declarations\n//=======================================================\n')
    v.write('\n\n\n\n')
    v.write('//=======================================================\n//  Structural coding\n//=======================================================\n')
    v.write('\n\n\n\n')
    v.write('endmodule\n')
    v.close()

def gerar_arquivo_vhdl(diretorio=''):
    projeto = get_nome_do_projeto()
    nome_arquivo = '{}.vhdl'.format(projeto)
    nome_arquivo = diretorio + '/' + nome_arquivo

    v = open(nome_arquivo, 'w')
    v.write('--=======================================================\n')
    v.write('-- This code is generated by Brena Marques\n')
    v.write('--=======================================================\n')
    v.write('library ieee;\n')
    v.write('use ieee.std_logic_1164.all;\n')
    v.write('entity {} is port(\n'.format(projeto))

    if check_clock.get():
        v.write('\t------------ CLOCK ----------\n')
        v.write('\tCLOCK_50MHz\t:in std_logic;\n\tCLK1_50\t:in std_logic;,\n\tMAX10_CLK2_50\tin std_logic;\n')
    
    if check_ext_clock.get(): 
        v.write('\n\t------------ EXT_CLK ----------\n')
        v.write('\tSMA_CLKIN \t\t       \t\t: in std_logic;\n')
        v.write('\tGPIO0_CLKIN\t\t         \t\t: in std_logic_vector(1 downto 0);\n')
        v.write('\tGPIO1_CLKIN\t\t      \t\t: in std_logic_vector(1 downto 0);\n')
        v.write('\tSMA_CLKOUT\t\t      \t\t: out std_logic;\n')
        v.write('\tGPIO0_CLKOUT\t\t      \t\t: out std_logic_vector(1 downto 0);\n')
        v.write('\tGPIO1_CLKOUT\t\t      \t\t: out std_logic_vector(1 downto 0);\n')

    if check_SW.get():
        v.write('\n\t------------ SW ----------\n')
        v.write('\tSW\t\t \t\t: in std_logic_vector(3 downto 0);\n')

    if check_chave.get():
        v.write('\n\t------------ KEY ----------\n')
        v.write('\tKEY\t\t  \t\t: in std_logic_vector(11 downto 0);\n')

    if check_LED_RGB.get():
        v.write('\n\t------------ LED_RGB ----------\n')
        v.write('\tLED_R\t\t          \t\t: out std_logic;\n')
        v.write('\tLED_G\t\t          \t\t: out std_logic;\n')
        v.write('\tLED_B\t\t          \t\t: out std_logic;\n')

    if check_segmentos.get():
        v.write('\n\t------------ SEG7 ----------\n')
        v.write('\tDISP0_D\t\t \t\t: out std_logic_vector(7 downto 0);\n')
        v.write('\tDISP1_D\t\t \t\t: out std_logic_vector(7 downto 0);\n')

    if check_LED_MATRIX.get():
        v.write('\n\t------------ LED_MATRIX ----------\n')
        v.write('\tLED_C\t\t \t\t: out std_logic_vector(4 downto 0);\n')
        v.write('\tLED_R\t\t \t\t: out std_logic_vector(7 downto 0);\n')

    if check_LCD.get():
        v.write('\n\t------------ LCD ----------\n')
        v.write('\tLCD_D\t\t          \t\t: inout std_logic_vector(7 downto 0);\n')
        v.write('\tLCD_RS\t\t      \t\t: out std_logic;\n')
        v.write('\tLCD_RW\t\t      \t\t: out std_logic;\n')
        v.write('\tLCD_EN\t\t      \t\t: out std_logic;\n')
        v.write('\tLCD_BACKLIGHT\t\t      \t\t: out std_logic;\n')

    if check_UART.get():
        v.write('\n\t------------ UART ----------\n')
        v.write('\tUART_TXD\t\t          \t\t: out std_logic;\n')
        v.write('\tUART_RXD\t\t          \t\t: in std_logic;\n')
        v.write('\tUART_CTS\t\t          \t\t: in std_logic;\n')
        v.write('\tUART_RTS\t\t          \t\t: out std_logic;\n')    

    if check_VGA.get():
        v.write('\n\t------------ VGA ----------\n')
        v.write('\tVGA_R\t\t      \t\t: out std_logic_vector(3 downto 0);\n')
        v.write('\tVGA_G\t\t      \t\t: out std_logic_vector(3 downto 0);\n')
        v.write('\tVGA_B\t\t      \t\t: out std_logic_vector(3 downto 0);\n')
        v.write('\tVGA_HS\t\t      \t\t: out std_logic;\n')
        v.write('\tVGA_VS\t\t      \t\t: out std_logic;\n')

    if check_SDRAM.get():
        v.write("------------ SDRAM ----------\n")
        v.write("\tDRAM_A\t\t\t: out std_logic_vector(12 downto 0);\n")
        v.write("\tDRAM_BA\t\t\t: out std_logic_vector(1 downto 0);\n")
        v.write("\tDRAM_CAS_N\t\t: out std_logic;\n")
        v.write("\tDRAM_CKE\t\t: out std_logic;\n")
        v.write("\tDRAM_CLK\t\t: out std_logic;\n")
        v.write("\tDRAM_CS_N\t\t: out std_logic;\n")
        v.write("\tDRAM_D\t\t\t: inout std_logic_vector(15 downto 0);\n")
        v.write("\tDRAM_RAS_N\t\t: out std_logic;\n")
        v.write("\tDRAM_DQM\t\t: out std_logic_vector(1 downto 0);\n")
        v.write("\tDRAM_WE_N\t\t: out std_logic;\n\n")

    if check_USB.get():
        v.write("------------ USB ----------\n")
        v.write("\tUSB_WR\t\t\t: out std std_logic;\n")
        v.write("\tUSB_RD\t\t\t: out std_logic;\n")
        v.write("\tUSB_D\t\t\t: inout std_logic_vector(7 downto 0);\n")
        v.write("\tUSB_POWEREN_N\t: in std_logic;\n")
        v.write("\tUSB_RXF_N\t\t: in std_logic;\n")
        v.write("\tUSB_TXE_N\t\t: in std_logic;\n\n")

    if check_SD_CARD.get():
        v.write("------------ SD_CARD ----------\n")
        v.write("\tSD_CMD\t\t\t: out std_logic;\n")
        v.write("\tSD_CLK\t\t\t: out std_logic;\n")
        v.write("\tSD_CD_N\t\t\t: out std_logic;\n")
        v.write("\tSD_D\t\t\t: inout std_logic_vector(3 downto 0);\n\n")
    
    if check_I2C.get():
        v.write("------------ I2C ----------\n")
        v.write("\tI2C_SDA\t\t\t: inout std_logic;\n")
        v.write("\tI2C_SCL\t\t\t: out std_logic;\n")
        v.write("\tI2C_OVERTEMP_N\t: in std_logic;\n\n")
    
    if check_Ethernet.get():
        v.write("------------ ETHERNET ----------\n")
        v.write("\tETH_TXEN\t\t: out std_logic;\n")
        v.write("\tETH_TXD\t\t: out std_logic_vector(3 downto 0);\n")
        v.write("\tETH_RXER\t\t: in std_logic;\n")
        v.write("\tETH_RXDV\t\t: in std_logic;\n")
        v.write("\tETH_RXD\t\t: in std_logic_vector(3 downto 0);\n")
        v.write("\tETH_MDIO\t\t: inout std_logic;\n")
        v.write("\tETH_MDC\t\t: out std_logic;\n")
        v.write("\tETH_CRS\t\t: in std_logic;\n")
        v.write("\tETH_COL\t\t: in std_logic;\n")
        v.write("\tETH_RST_N\t\t: out std_logic;\n")
        v.write("\tETH_RXCLK\t\t: in std_logic;\n")
        v.write("\tETH_TXCLK\t\t: in std_logic;\n")
        v.write("\tETH_TXER\t\t: out std_logic;\n\n")

    if check_ADC.get():
        v.write("------------ ADC ----------\n")
        v.write("\tADC_CNVST\t\t: out std_logic;\n")
        v.write("\tADC_CS_N\t\t: out std_logic;\n")
        v.write("\tADC_DOUT1\t\t: in std_logic;\n")
        v.write("\tADC_DOUT2\t\t: in std_logic;\n")
        v.write("\tADC_REFSEL\t\t: out std_logic;\n")
        v.write("\tADC_SCLK\t\t: out std_logic;\n")
        v.write("\tADC_SD\t\t\t: out std_logic;\n")
        v.write("\tADC_SEL\t\t: out std_logic;\n")
        v.write("\tADC_UB\t\t\t: out std_logic;\n\n")

    if check_DAC.get():
        v.write('\n\t------------ DAC ----------\n')
        v.write('\tDAC_CLR\t\t          \t\t: out std_logic;\n')
        v.write('\tDAC_CS_N\t\t      \t\t: out std_logic;\n')
        v.write('\tDAC_DIN\t\t      \t\t: out std_logic;\n')
        v.write('\tDAC_SCLK\t\t      \t\t: out std_logic;\n')

    if check_flash.get():
        v.write('\n\t------------ FLASH ----------\n')
        v.write('\tFLASH_ASDO\t\t          \t\t: out std_logic;\n')
        v.write('\tFLASH_CS0_N\t\t      \t\t: out std_logic;\n')
        v.write('\tFLASH_DATA0\t\t      \t\t: inout std_logic;\n')
        v.write('\tFLASH_DCLK\t\t      \t\t: out std_logic;\n')

    if check_PROTO_A.get():
        v.write('\n\t------------ PROTO_A ----------\n')
        v.write('\tPROTO_A\t\t          \t\t: inout std_logic_vector(7 downto 0);\n')

    if check_PROTO_B.get():
        v.write('\n\t------------ PROTO_B ----------\n')
        v.write('\tPROTO_B\t\t          \t\t: inout std_logic_vector(7 downto 0);\n')

    if check_GPIO.get():
        v.write('\n\t------------ GPIO, GPIO connect SA-SB ----------\n')
        v.write('\tSA\t\t      \t\t: in std_logic_vector(7 downto 0);\n')
        v.write('\tSB\t\t  \t\t: in std_logic_vector(7 downto 0);\n')
        
    if check_ConnectGPIO.get():
        v.write('\n\t------------ GPIO, GPIO connect to GPIO Default ----------\n')
        v.write('\tGPIO_D\t\t          \t\t: inout std_logic_vector(35 downto 0)\n')

    v.write(');\n')
    v.write("end entity MERCURIO_IV_FULL;\n")
    v.write("architecture systembuilder of MERCURIO_IV_FULL is\n")
    v.write("--=======================================================\n\n")
    v.write('--  SIGNAL, CONSTANT, COMPONENT, FUNCTION declarations\n')
    v.write('--=======================================================\n')
    v.write('begin\n')
    v.write('--=======================================================\n')
    v.write('--  Structural coding\n')
    v.write('--=======================================================\n')
    v.write('\n\n')
    v.write('end architecture systembuilder;\n')
    v.close()


def gerar_arquivo_sdc(diretorio=''):
    projeto = get_nome_do_projeto()
    nome_arquivo = '{}.sdc'.format(projeto)
    nome_arquivo = diretorio + '/' + nome_arquivo

    if check_clock.get():
        f = open('auxiliar/com_clock.sdc', 'r')
        buffer = f.read()
        f.close()
    else:
        f = open('auxiliar/sem_clock.sdc', 'r')
        buffer = f.read()
        f.close()

    sdc = open(nome_arquivo, 'w')
    sdc.write(buffer)
    sdc.close()


def gerar_codigo():
    diretorio = get_diretorio_arquivos()

    gerar_arquivo_qpf(diretorio)
    gerar_arquivo_qsf(diretorio)
    gerar_arquivo_sdc(diretorio)
    if check_v.get():
        gerar_arquivo_v(diretorio)
    if check_vhdl.get():
        gerar_arquivo_vhdl(diretorio)


def gerar_botoes_rodape(frame, padding_x=40, ipad_x=10):
    Button(frame, text="Salvar Configuração", command=get_estados).grid(row=0, column=0, padx=padding_x, pady=3, ipadx=ipad_x)
    Button(frame, text="Carregar Configuração", command=set_estados).grid(row=0, column=1, padx=padding_x, pady=3, ipadx=ipad_x)
    Button(frame, text="Gerar", command=gerar_codigo).grid(row=0, column=2, padx=padding_x, pady=3, ipadx=ipad_x)
    Button(frame, text="Sair", command=window.destroy).grid(row=0, column=3, padx=padding_x, pady=3, ipadx=ipad_x)


def gerar_rodape(largura, altura, background_color):
    frame_rodape = Frame(window, width=largura, height=altura, bg=background_color)
    frame_rodape.pack(fill=X, side=BOTTOM)
    gerar_botoes_rodape(frame_rodape)


def get_estados():
    estados = {
        'projeto_nome': get_nome_do_projeto(),
        'check_v':check_v.get(),
        'check_vhdl':check_vhdl.get(),
        'check_clock': check_clock.get(),
        'check_SDRAM_64': check_SDRAM.get(),
        'check_segmentos': check_segmentos.get(),
        'check_chave': check_chave.get(),
        'check_LED': check_LED_MATRIX.get(),
        'check_button': check_button.get(),
        'check_VGA': check_VGA.get(),
        'check_GPIO': check_GPIO.get(),
        'check_LCD': check_LCD.get(),
        'check_Ethernet': check_Ethernet.get(),
        'check_I2C': check_I2C.get(),
        'check_RS232': check_RS232.get(),
        'check_micro_SD': check_SD_CARD.get(),
        'check_SDRAM_512': check_PROTO_A.get(),
        'check_SDRAM_512': check_PROTO_B.get(),
        'check_PMOD': check_PMOD.get(),
        'check_flash_64': check_flash.get(),
        'check_LED_RGB': check_LED_RGB.get(),
        'check_ADC': check_ADC.get(),
        'check_DAC': check_DAC.get(),
        'check_SA_SB': check_SA_SB.get(),
        'check_SW' : check_SW(),
        'check_ConnectGPIO':check_ConnectGPIO()
    }

    tipo_do_arquivo = (('text files', '.json'), ('All files', '*.*'))

    arquivo = fd.asksaveasfile(mode='w', filetypes=tipo_do_arquivo, defaultextension='.json')

    if arquivo is None:  # asksaveasfile return `None` if dialog closed with "cancel".
        return

    json.dump(estados, arquivo)


def set_estados():
    with open(get_arquivo('.json')) as f:
        data = json.load(f)

    nome_do_projeto.set(data['projeto_nome'])

    check_vhdl.set(data['check_vhdl'])
    check_v.set(data['check_v'])
    check_clock.set(data['check_clock'])
    check_SDRAM.set(data['check_SDRAM_64'])
    check_segmentos.set(data['check_segmentos'])
    check_chave.set(data['check_chave'])
    check_LED_MATRIX.set(data['check_LED'])
    check_button.set(data['check_button'])
    check_VGA.set(data['check_VGA'])
    check_GPIO.set(data['check_GPIO'])
    check_LCD.set(data['check_LCD'])
    check_Ethernet.set(data['check_Ethernet'])
    check_I2C.set(data['check_I2C'])
    check_RS232.set(data['check_RS232'])
    check_SD_CARD.set(data['check_micro_SD'])
    check_PROTO_A.set(data['check_SDRAM_512'])
    check_PROTO_B.set(data['check_SDRAM_512'])
    check_PMOD.set(data['check_PMOD'])
    check_flash.set(data['check_flash_64'])
    check_LED_RGB.set(data['check_LED_RGB'])
    check_ADC.set(data['check_ADC'])
    check_DAC.set(data['check_DAC'])
    check_SA_SB.set(data['check_SA_SB'])
    check_SW.set(data['check_SW'])
    check_ConnectGPIO.set(data['check_ConnectGPIO'])


frame_selecao = LabelFrame(window, width=350, height=410, text="Configurações do Sistema")

gerar_rodape(350, 50, "#f0f0f0")

frame_imagem = LabelFrame(window, width=380, height=410, text="Cyclone IV")
image = ImageTk.PhotoImage(Image.open("assets/img.png"))
Label(frame_imagem, image=image).place(relx=0.5, rely=0.5, anchor=CENTER)
frame_imagem.pack(fill=X, side=LEFT)

frame_selecao.pack(fill=X, side=LEFT)
Label(frame_selecao, text="Nome do Projeto:").place(relx=0.05, anchor='nw')
Entry(frame_selecao, width=40, textvariable=nome_do_projeto).place(relx=0.05, rely=0.06, anchor='nw')

criar_selecao('VERILOG', check_v,1, 2)
criar_selecao('CLOCK', check_clock, 1, 3)
criar_selecao('LED 8X5', check_LED_MATRIX, 1, 4)
criar_selecao('Botão x12', check_button, 1, 5)
criar_selecao('VGA', check_VGA, 1, 6)
criar_selecao('LCD', check_LCD, 1, 7)
criar_selecao('SDRAM 512Mbit', check_SDRAM, 1, 8)
criar_selecao('Conector Micro SD', check_SD_CARD, 1, 9)
criar_selecao('Serial RS232', check_RS232, 1, 10)
criar_selecao('Sensor de temperatura I²C', check_I2C, 1, 11)
criar_selecao('10/100 Ethernet PHY', check_Ethernet, 1, 12)
criar_selecao('SW', check_SW, 1, 13)

criar_selecao('VHDL', check_vhdl,2, 2)
criar_selecao('7-Segmentos X 2', check_segmentos, 2, 3)
criar_selecao('Chave X4', check_chave, 2, 4)
criar_selecao('Conector 2x GPIO', check_GPIO, 2, 5)
criar_selecao('SDRAM, 64 MB', check_PROTO_A, 2, 6)
criar_selecao('SA e SB', check_SA_SB, 2, 7)
criar_selecao('DAC', check_DAC, 2, 8)
criar_selecao('ADC', check_ADC, 2, 9)
criar_selecao('LED RGB', check_LED_RGB, 2, 10)
criar_selecao('FLASH 64Mbit', check_flash, 2, 11)
criar_selecao('PMOD x2', check_PMOD, 2, 12)
criar_selecao('ConnectGPIO', check_ConnectGPIO, 2, 13)

window.resizable(False, False)
window.mainloop()
