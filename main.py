from PyQt5 import QtWidgets, uic
from Classes import *
import random
import re
import sys

# спользовать модуль keyboard


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # Загрузить .ui файл
        uic.loadUi("FW_0.0.4.ui", self)
        # Привязать метод к кнопке
        self.pushButton_2.clicked.connect(self.on_button_click)

        list_of_protocols = ['CLNS', 'DDP', 'EGP', 'EIGRP', 'ICMP', 'IGMP']
        list_of_ports = ['FTP', 'SMTP', 'SSH', 'HTTP', 'HTTPS', 'POP']
        self.all_comps = []
        comps_protected = ''
        comps_non_protected = ''
        self.all_protected_comps = []
        self.all_non_protected_comps = []
        self.black_list = []

        for i in range (random.randint (2, 5)):
            nm = f"Computer{chr (i + 65)}"
            comp = Computer (nm)
            self.all_comps.append (comp)
            self.all_protected_comps.append (comp)
            comp.is_protected = True
            comp.gen_ip ()
            comp.supported_protocols = random.sample (list_of_protocols, k=random.randint (2, 4))
            comp.ports = random.sample (list_of_ports, k=random.randint (2, 4))
            #sp = ', '.join(comp.supported_protocols)
            #p = ', '.join(comp.ports)

            #comps_protected += f'{comp.__name__}    {comp.ip_address}  Порты: {p} \n' \
            #                       f'Протоколы: {sp}\n\n'

        for j in range (random.randint (2, 5)):
            nm = f"Computer{j + 1}"
            comp = Computer (nm)
            self.all_comps.append (comp)
            self.all_non_protected_comps.append (comp)
            comp.is_protected = False
            comp.gen_ip ()
            comp.supported_protocols = random.sample (list_of_protocols, k=random.randint (2, 4))
            comp.ports = random.sample (list_of_ports, k=random.randint (2, 4))

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

        #ПЕРЕДВИНУТЬ ПРОВЕРКУ И СДЕЛАТЬ ВЫВОД ТЕКСТА ПОСЛЕ НЕЕ


        self.label_secure_comp.setText(f"{comps_protected}")
        self.label_non_secure_comp.setText(f"{comps_non_protected}")
        self.label_task_text.setText(f"   Отправить данные с компьютера {self.protected_comp_for_task.__name__} на {self.non_protected_comp_for_task.__name__}")


    def ip_range(self, ip, range_start, range_end):
        ip_nums = ip.split('.')
        start = range_start.split('.')
        end = range_end.split('.')
        return int(start[0]) <= int(ip_nums[0]) <= int(end[0]) and int(start[1]) <= int(ip_nums[1]) <= int(end[1]) and \
               int(start[2]) <= int(ip_nums[2]) <= int(end[2]) and int(start[3]) <= int(ip_nums[3]) <= int(end[3])

    def check(self, computer, access_destination, access_source, access_net_protocol, access_ports):
        if computer.ip_address in self.black_list:
            computer.is_allowed = False
            return
        source_range, destination_range = False, False
        if len(access_source) == 2:
            source_range = True
        if len(access_destination) == 2:
            destination_range = True

        if source_range and computer.is_protected:
            if self.ip_range(computer.ip_address, access_source[0], access_source[1]): # здесь учитываем только отправителей
                    chk1 = False
                    for pr in computer.supported_protocols:
                        if pr in access_net_protocol:
                            chk1 = True
                            break
                    chk2 = False
                    for port in computer.ports:
                        if port == access_ports[0]:
                            chk2 = True
                    if chk1 and chk2:  # условие разрешения соединения  ВЕРНУТЬ and chk2
                        computer.is_allowed = True
                        computer.is_connected_before = True

        if destination_range and not computer.is_protected:
            if self.ip_range(computer.ip_address, access_destination[0], access_destination[1]):
                chk1 = False
                for pr in computer.supported_protocols:
                    if pr in access_net_protocol:
                        chk1 = True
                        break
                chk2 = False
                for port in computer.ports:
                    if port == access_ports[0]:
                        chk2 = True
                if chk1 and chk2:  # условие разрешения соединения  ВЕРНУТЬ and chk2
                    computer.is_allowed = True
                    computer.is_connected_before = True

        elif computer.ip_address in (access_source):
            if not computer.is_protected:  # здесь учитываем только отправителей
                return
            chk1 = False
            for pr in computer.supported_protocols:
                if pr in access_net_protocol:
                    chk1 = True
                    break
            chk2 = False
            for port in computer.ports:
                if port == access_ports[0]:
                    chk2 = True
            if chk1 and chk2:  # условие разрешения соединения  ВЕРНУТЬ and chk2
                computer.is_allowed = True
                computer.is_connected_before = True

        elif computer.ip_address in (access_destination):
            if computer.is_protected:  # здесь учитываем только получателей
                return
            chk1 = False
            for pr in computer.supported_protocols:
                if pr in access_net_protocol:
                    chk1 = True
                    break
            chk2 = False
            for port in computer.ports:
                if port == access_ports[0]:
                    chk2 = True
            if chk1 and chk2:  # условие разрешения соединения  ВЕРНУТЬ and chk2
                computer.is_allowed = True
                computer.is_connected_before = True

    def on_button_click(self):

        user_input = self.textEdit.toPlainText ()
        commands = user_input.splitlines ()
        print (commands)

        access_destination = []
        access_source = []
        access_net_protocol = []
        access_ports = []

        #!!! КОМАНДЫ ДЛЯ ВВОДА В ТЕКСТОВОЕ ПОЛЕ ПОЛЬЗОВАТЕЛЕМ:
        #
        #   set ip sender 000.000.000.000 / set ip sender range 000.000.000.000 255.255.255.255
        #   set ip receiver 000.000.000.000 / set ip receiver range 000.000.000.000 255.255.255.255
        #   set ports AAA, BBB, CCC
        #   set protocol AAA, BBB, CCC
        #   block ip 000.000.000.000
        #   remove ports AAA, CCC
        #   remove protocol AAA, CCC
        #   clear ip
        #   clear ports
        #   clear protocol
        # ip_add = re.search(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', command)


        for command in commands:
            if re.search(r'set ip sender', command):
                access_source = (re.findall (r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', command))

            elif re.search(r'set ip sender range', command):
                access_source = (re.findall (r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', command))

            elif re.search(r'set ip receiver', command):
                access_destination = (re.findall (r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', command))

            elif re.search(r'set ip receiver range', command):
                access_destination = (re.findall (r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', command))

            elif re.search(r'set ports', command):
                access_ports = (re.findall (r'\b[A-Z]{2,5}\b', command))

            elif re.search(r'set protocol', command):
                access_net_protocol = (re.findall (r'\b[A-Z]{2,5}\b', command))

            elif re.search(r'block ip', command):
                self.black_list += (re.findall(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', command))[0]

            elif re.search(r'remove ports', command):
                for prt in (re.findall(r'\b[A-Z]{2,5}\b', command)):
                    access_net_protocol.remove(prt)

            elif re.search(r'remove protocol', command):
                for prt in (re.findall (r'\b[A-Z]{2,5}\b', command)):
                    access_net_protocol.remove (prt)

            elif re.search(r'clear ip', command):
                access_source = []
                access_destination = []

            elif re.search(r'clear ports', command):
                access_ports = []

            elif re.search(r'clear protocol', command):
                access_net_protocol = []

            else:
                continue

        print(access_source)
        print(access_destination)
        print(access_net_protocol)
        print(access_ports)

        checker = 0
        for comp in self.all_comps:
            self.check (comp, access_destination, access_source, access_net_protocol, access_ports)
            print (comp.__name__, comp.is_allowed)
            if (comp.__name__ == self.protected_comp_for_task.__name__
                    or comp.__name__ == self.non_protected_comp_for_task.__name__) \
                    and comp.is_allowed:
                checker += 1
        if checker == 2:
            self.correct_answer.setStyleSheet ('color : green')
            self.wrong_answer.setStyleSheet ('color : black')
        else:
            self.wrong_answer.setStyleSheet ('color : red')


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
