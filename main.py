from PyQt5 import QtWidgets, uic
from PyQt5.Qt import Qt
from Classes import *
from Help import Ui_Help
import random
import re
import sys
from getkey import getkey, keys
import keyboard



class MainWindow(QtWidgets.QMainWindow):

    def open_help_window(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Help()
        self.ui.setupUi(self.window)
        self.window.show()


    # ФУНКЦИИ ЛОГИКИ

    def ip_range(self, ip, range_start, range_end):
        ip_nums = ip.split('.')
        start = range_start.split('.')
        end = range_end.split('.')
        return int(start[0]) <= int(ip_nums[0]) <= int(end[0]) and int(start[1]) <= int(ip_nums[1]) <= int(end[1]) and \
               int(start[2]) <= int(ip_nums[2]) <= int(end[2]) and int(start[3]) <= int(ip_nums[3]) <= int(end[3])

    def generate_computer(self, name_suffix, is_protected):
        nm = f"Computer{name_suffix}"
        comp = Computer (nm)
        self.all_comps.append (comp)

        if is_protected:
            self.all_protected_comps.append (comp)
            comp.is_protected = True
        else:
            self.all_non_protected_comps.append (comp)
            comp.is_protected = False

        comp.gen_ip ()
        comp.supported_protocols = random.sample (self.list_of_protocols, k=random.randint (2, 4))
        comp.ports = random.sample (self.list_of_ports, k=random.randint (2, 4))

    def on_press_enter(self):

        self.user_input = self.lineEdit.text()
        self.lineEdit.setText('')
        self.text_prev_commands += f'{self.user_input}\n'
        self.textEdit.setPlainText(self.text_prev_commands)



    def getting_commands(self):
        commands_mapping = {
            'set ip sender': self.set_ip_sender,
            'set ip sender range': self.set_ip_sender,
            'set ip receiver': self.set_ip_receiver,
            'set ip receiver range': self.set_ip_receiver,
            'set ports': self.set_ports,
            'set protocol': self.set_protocol,
            'block ip': self.block_ip,
            'remove ports': self.remove_ports,
            'remove protocol': self.remove_protocol,
            'clear ip': self.clear_ip,
            'clear ports': self.clear_ports,
            'clear protocol': self.clear_protocol
        }

        commands = self.text_prev_commands.splitlines ()

        for command in commands:
            for keyword, action in commands_mapping.items ():
                if re.search (keyword, command):
                    action (command)
                    break

    def set_ip_sender(self, command):
        self.access_source = re.findall (r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', command)

    def set_ip_receiver(self, command):
        self.access_destination = (re.findall (r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', command))

    def set_ports(self, command):
        self.access_ports += (re.findall (r'\b[A-Z]{2,5}\b', command))

    def set_protocol(self, command):
        self.access_net_protocol += (re.findall (r'\b[A-Z]{2,5}\b', command))

    def block_ip(self, command):
        self.black_list += (re.findall(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', command)) #[0]

    def remove_ports(self, command):
        for prt in (re.findall (r'\b[A-Z]{2,5}\b', command)):
            try:
                self.access_ports.remove (prt)
            except:
                continue

    def remove_protocol(self, command):
        for prt in (re.findall (r'\b[A-Z]{2,5}\b', command)):
            try:
                self.access_net_protocol.remove (prt)
            except:
                continue

    def clear_ip(self, command):
        self.access_source = []
        self.access_destination = []

    def clear_ports(self, command):
        self.access_ports = []

    def clear_protocol(self, command):
        self.access_net_protocol = []



    def check(self, computer):

        print('Вызов кнопкой')
        print (self.access_source)
        print (self.access_destination)
        print (self.access_net_protocol)
        print (self.access_ports)

        # Если IP компьютера в чёрном списке, блокируем его
        if computer.ip_address in self.black_list:
            computer.is_allowed = False
            return

        # Проверяем доступ по источнику
        if self.access_source and computer.is_protected and len (self.access_source) == 2:
            if self.ip_range (computer.ip_address, self.access_source[0], self.access_source[1]):
                computer.is_allowed = any (pr in self.access_net_protocol for pr in computer.supported_protocols) and self.access_ports in computer.ports

        # Проверяем доступ по приемнику
        elif self.access_destination and not computer.is_protected and len (self.access_destination) == 2:
            if self.ip_range (computer.ip_address, self.access_destination[0], self.access_destination[1]):
                computer.is_allowed = any (pr in self.access_net_protocol for pr in computer.supported_protocols) and self.access_ports in computer.ports

        # Проверяем общий доступ по IP
        elif self.access_source and not computer.is_protected and computer.ip_address in self.access_source:
            computer.is_allowed = any (pr in self.access_net_protocol for pr in computer.supported_protocols) and self.access_ports in computer.ports

        # Проверяем общий доступ по IP
        elif self.access_destination and computer.is_protected and computer.ip_address in self.access_destination:
            computer.is_allowed = any (pr in self.access_net_protocol for pr in computer.supported_protocols) and self.access_ports in computer.ports


        # if computer.ip_address in self.black_list:
        #     computer.is_allowed = False
        #     return
        # source_range, destination_range = False, False
        # if len(self.access_source) == 2:
        #     source_range = True
        # if len(self.access_destination) == 2:
        #     destination_range = True
        #
        # if source_range and computer.is_protected:
        #     if self.ip_range(computer.ip_address, self.access_source[0], self.access_source[1]): # здесь учитываем только отправителей
        #             chk1 = False
        #             for pr in computer.supported_protocols:
        #                 if pr in self.access_net_protocol:
        #                     chk1 = True
        #                     break
        #             chk2 = False
        #             for port in computer.ports:
        #                 if port == self.access_ports:
        #                     chk2 = True
        #             if chk1 and chk2:  # условие разрешения соединения  ВЕРНУТЬ and chk2
        #                 computer.is_allowed = True
        #                 computer.is_connected_before = True
        #
        # if destination_range and not computer.is_protected:
        #     if self.ip_range(computer.ip_address, self.access_destination[0], self.access_destination[1]):
        #         chk1 = False
        #         for pr in computer.supported_protocols:
        #             if pr in self.access_net_protocol:
        #                 chk1 = True
        #                 break
        #         chk2 = False
        #         for port in computer.ports:
        #             if port == self.access_ports:
        #                 chk2 = True
        #         if chk1 and chk2:  # условие разрешения соединения  ВЕРНУТЬ and chk2
        #             computer.is_allowed = True
        #             computer.is_connected_before = True
        #
        # elif computer.ip_address in (self.access_source):
        #     if not computer.is_protected:  # здесь учитываем только отправителей
        #         return
        #     chk1 = False
        #     for pr in computer.supported_protocols:
        #         if pr in self.access_net_protocol:
        #             chk1 = True
        #             break
        #     chk2 = False
        #     for port in computer.ports:
        #         if port == self.access_ports:
        #             chk2 = True
        #     if chk1 and chk2:  # условие разрешения соединения  ВЕРНУТЬ and chk2
        #         computer.is_allowed = True
        #         computer.is_connected_before = True
        #
        # elif computer.ip_address in (self.access_destination):
        #     if computer.is_protected:  # здесь учитываем только получателей
        #         return
        #     chk1 = False
        #     for pr in computer.supported_protocols:
        #         if pr in self.access_net_protocol:
        #             chk1 = True
        #             break
        #     chk2 = False
        #     for port in computer.ports:
        #         if port == self.access_ports:
        #             chk2 = True
        #     if chk1 and chk2:  # условие разрешения соединения
        #         computer.is_allowed = True
        #         computer.is_connected_before = True

    def on_button_press(self):
        self.getting_commands ()
        for comp in self.all_comps:
            self.check(comp)
            print(f"{comp.__name__} {comp.is_allowed}")



    def __init__(self):
        super(MainWindow, self).__init__()
        # Загрузить .ui файл
        uic.loadUi("FW_0.0.5.ui", self)

        self.text_prev_commands = ''  # хранение истории ввода
        self.user_input = ''          # нынешняя введенная строка

        self.pushButton.clicked.connect (self.open_help_window)
        self.pushButton_2.clicked.connect (self.on_button_press)
        self.lineEdit.returnPressed.connect (self.on_press_enter)

        self.list_of_protocols = ['CLNS', 'DDP', 'EGP', 'EIGRP', 'ICMP', 'IGMP']
        self.list_of_ports = ['FTP', 'SMTP', 'SSH', 'HTTP', 'HTTPS', 'POP']
        self.all_comps = []
        comps_protected = ''
        comps_non_protected = ''
        self.all_protected_comps = []
        self.all_non_protected_comps = []
        self.black_list = []

        self.access_destination = []
        self.access_source = []
        self.access_net_protocol = []
        self.access_ports = []

        # Генерация защищенных компьютеров
        for i in range (random.randint (2, 5)):
            self.generate_computer (chr (i + 65), is_protected=True)

        # Генерация не защищенных компьютеров
        for j in range (random.randint (2, 5)):
            self.generate_computer (str (j + 1), is_protected=False)

        self.protected_comp_for_task = random.choice (self.all_protected_comps)
        self.non_protected_comp_for_task = random.choice (self.all_non_protected_comps)

        self.sublist_common_protocols = list (set (self.protected_comp_for_task.supported_protocols) & set (
            self.non_protected_comp_for_task.supported_protocols))
        if not self.sublist_common_protocols:
            self.protected_comp_for_task.supported_protocols.append (
                self.non_protected_comp_for_task.supported_protocols[0])

        self.sublist_common_ports = list (set (self.protected_comp_for_task.ports) & set (
            self.non_protected_comp_for_task.ports))
        if not self.sublist_common_ports:
            self.protected_comp_for_task.ports.append (
                self.non_protected_comp_for_task.ports[0])

        for comp in self.all_protected_comps:
            sp = ', '.join (comp.supported_protocols)
            p = ', '.join (comp.ports)

            comps_protected += f'{comp.__name__}    {comp.ip_address}  Порты: {p} \n' \
                                   f'Протоколы: {sp}\n\n'

        for comp in self.all_non_protected_comps:
            sp = ', '.join (comp.supported_protocols)
            p = ', '.join (comp.ports)

            comps_non_protected += f'{comp.__name__}    {comp.ip_address}  Порты: {p} \n' \
                                   f'Протоколы: {sp}\n\n'


        self.label_secure_comp.setText(f"{comps_protected}")
        self.label_non_secure_comp.setText(f"{comps_non_protected}")
        self.label_task_text.setText(f"   Отправить данные с компьютера {self.protected_comp_for_task.__name__} на {self.non_protected_comp_for_task.__name__}")







if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()