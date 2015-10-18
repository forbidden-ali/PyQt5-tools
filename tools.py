# -*- coding: utf-8 -*-

"""
Module implementing switch.
"""
import sys
from base64 import b64encode,  b64decode
from binascii import hexlify,  unhexlify
from urllib import parse
import secret
from PyQt5.QtCore import pyqtSlot,  QUrl
from PyQt5.QtWidgets import QWidget,  QApplication

from HashIdentifier import *
from Ui_tools import Ui_Form


class switch(QWidget, Ui_Form):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (QWidget)
        """
        super(switch, self).__init__(parent)
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
    
    @pyqtSlot()
    def on_b1_clicked(self):
        self.stackedWidget.setCurrentIndex(0)
        
    def on_code_currentIndexChanged(self):
        self.stackedWidget_2.setCurrentIndex(self.code.currentIndex())
        
    def on_s2_p1_b1_clicked(self):
        self.s2_p1_t2.setText(parse.quote(self.s2_p1_t1.toPlainText()))
        
    def on_s2_p1_b2_clicked(self):
        self.s2_p1_t1.setText(parse.unquote(self.s2_p1_t2.toPlainText()))
        
    def on_s2_p2_b1_clicked(self):
        self.s2_p2_t2.setText(b64encode(self.s2_p2_t1.toPlainText().encode(encoding="utf-8")).decode())
        
    def on_s2_p2_b2_clicked(self):
        self.s2_p2_t1.setText(b64decode(self.s2_p2_t2.toPlainText().encode(encoding="utf-8")).decode())
        
    def on_s2_p3_b1_clicked(self):
        self.s2_p3_t2.setText(hexlify(self.s2_p3_t1.toPlainText().encode(encoding="utf-8")).decode())
        
    def on_s2_p3_b2_clicked(self):
        self.s2_p3_t1.setText(unhexlify(self.s2_p3_t2.toPlainText().encode(encoding="utf-8")).decode())
        
    @pyqtSlot()
    def on_b2_clicked(self):
        self.stackedWidget.setCurrentIndex(1)
        self.webView_1.setUrl(QUrl('http://www.aizhan.com'))
        
    def on_tabWidget_currentChanged(self):
        if self.tabWidget.currentIndex() == 0:
            self.webView_1.setUrl(QUrl('http://www.aizhan.com'))
        elif self.tabWidget.currentIndex() == 1:
            self.webView_2.setUrl(QUrl('http://tool.chinaz.com'))            
        elif self.tabWidget.currentIndex() == 2:
            self.webView_3.setUrl(QUrl('http://www.alexa.cn'))   
        else:
            pass    
            
    @pyqtSlot()
    def on_b3_clicked(self):
        self.stackedWidget.setCurrentIndex(2)
        self.p3_w1.setUrl(QUrl('http://www.cmd5.com'))
        
    def on_p3_b1_clicked(self):
        has = self.p3_l1.text()
        ADLER32(has); CRC16(has); CRC16CCITT(has); CRC32(has); CRC32B(has); DESUnix(has); DomainCachedCredentials(has); FCS16(has); GHash323(has); GHash325(has); GOSTR341194(has); Haval128(has); Haval128HMAC(has); Haval160(has); Haval160HMAC(has); Haval192(has); Haval192HMAC(has); Haval224(has); Haval224HMAC(has); Haval256(has); Haval256HMAC(has); LineageIIC4(has); MD2(has); MD2HMAC(has); MD4(has); MD4HMAC(has); MD5(has); MD5APR(has); MD5HMAC(has); MD5HMACWordpress(has); MD5phpBB3(has); MD5Unix(has); MD5Wordpress(has); MD5Half(has); MD5Middle(has); MD5passsaltjoomla1(has); MD5passsaltjoomla2(has); MySQL(has); MySQL5(has); MySQL160bit(has); NTLM(has); RAdminv2x(has); RipeMD128(has); RipeMD128HMAC(has); RipeMD160(has); RipeMD160HMAC(has); RipeMD256(has); RipeMD256HMAC(has); RipeMD320(has); RipeMD320HMAC(has); SAM(has); SHA1(has); SHA1Django(has); SHA1HMAC(has); SHA1MaNGOS(has); SHA1MaNGOS2(has); SHA224(has); SHA224HMAC(has); SHA256(has); SHA256s(has); SHA256Django(has); SHA256HMAC(has); SHA256md5pass(has); SHA256sha1pass(has); SHA384(has); SHA384Django(has); SHA384HMAC(has); SHA512(has); SHA512HMAC(has); SNEFRU128(has); SNEFRU128HMAC(has); SNEFRU256(has); SNEFRU256HMAC(has); Tiger128(has); Tiger128HMAC(has); Tiger160(has); Tiger160HMAC(has); Tiger192(has); Tiger192HMAC(has); Whirlpool(has); WhirlpoolHMAC(has); XOR32(has); md5passsalt(has); md5saltmd5pass(has); md5saltpass(has); md5saltpasssalt(has); md5saltpassusername(has); md5saltmd5pass(has); md5saltmd5passsalt(has); md5saltmd5passsalt(has); md5saltmd5saltpass(has); md5saltmd5md5passsalt(has); md5username0pass(has); md5usernameLFpass(has); md5usernamemd5passsalt(has); md5md5pass(has); md5md5passsalt(has); md5md5passmd5salt(has); md5md5saltpass(has); md5md5saltmd5pass(has); md5md5usernamepasssalt(has); md5md5md5pass(has); md5md5md5md5pass(has); md5md5md5md5md5pass(has); md5sha1pass(has); md5sha1md5pass(has); md5sha1md5sha1pass(has); md5strtouppermd5pass(has); sha1passsalt(has); sha1saltpass(has); sha1saltmd5pass(has); sha1saltmd5passsalt(has); sha1saltsha1pass(has); sha1saltsha1saltsha1pass(has); sha1usernamepass(has); sha1usernamepasssalt(has); sha1md5pass(has); sha1md5passsalt(has); sha1md5sha1pass(has); sha1sha1pass(has); sha1sha1passsalt(has); sha1sha1passsubstrpass03(has); sha1sha1saltpass(has); sha1sha1sha1pass(has); sha1strtolowerusernamepass(has)
        
        if len(jerar)==0:
            ans = 'Not Found.'
        elif len(jerar)>2:
            jerar.sort()
            lea = ''
            lea1 = ''
            for a in range(int(len(jerar))-2):
                lea1 = '\n'+"[+] "+algorithms[jerar[a+2]]
                lea = lea + lea1
            ans = "Possible Hashs:"+'\n'+"[+] "+algorithms[jerar[0]]+'\n'+"[+] "+algorithms[jerar[1]]+'\n'+"Least Possible Hashs:"+lea
        else:
            jerar.sort()
            lea = ''
            lea1 = ''
            for a in range(len(jerar)):
                lea1 = "[+] ",algorithms[jerar[a]]+'\n'
                lea = lea + lea1
            ans = "Possible Hashs:"+'\n'+ lea
        self.p3_t1.setText(ans)
        
    @pyqtSlot()
    def on_b4_clicked(self):
        self.stackedWidget.setCurrentIndex(3)
        self.stackedWidget_3.setCurrentIndex(0)
        self.s3_p1_r1.setChecked(True)
        self.s3_p1_r5.setChecked(True)
        
    def on_s3_p1_b1_clicked(self):
        self.stackedWidget_3.setCurrentIndex(1)
        lev = 0
        secre = ''
        qq = []
        mob = []
        if self.s3_p1_r5.isChecked():
            lev = 30
        if self.s3_p1_r6.isChecked():   
            lev = 100
        if self.s3_p1_r7.isChecked():            
            lev = 200
        if self.s3_p1_r8.isChecked():
            lev = 600
        if (self.s3_p1_e5.text() != ''):
            qq = secret.qq(self.s3_p1_e5.text()) 
        if (self.s3_p1_e6.text() != ''):
            qq = qq + secret.qq(self.s3_p1_e6.text())
        if (self.s3_p1_e4.text() != ''):
            mob = secret.mob(self.s3_p1_e4.text())
        if (self.s3_p1_e16.text() != ''):
            mob = mob + secret.mob(self.s3_p1_e16.text())
        if (self.s3_p1_e20.text() != ''):
            mob = mob + secret.mob(self.s3_p1_e20.text())
        if (self.s3_p1_e24.text() != ''):
            mob = mob + secret.mob(self.s3_p1_e24.text())
        li = qq + mob
        
        if self.s3_p1_r1.isChecked():
            secre = secret.secr(li, lev, 6)
            print(secre)
            print('\n'.join(secre))
            self.s3_p2_t1.setText('\n'.join(secre))
        if self.s3_p1_r2.isChecked():
            secre = secret.secr(li, lev, 8)
            self.s3_p2_t1.setText('\n'.join(secre))
        if self.s3_p1_r3.isChecked():
            secre = secret.secr(li, lev, 7)
            secre = secre + secret.secr(li, lev, 8)
            secre = secre + secret.secr(li, lev, 9)
            secre = secre + secret.secr(li, lev, 10)
            secre = secre + secret.secr(li, lev, 11)
            self.s3_p2_t1.setText('\n'.join(secre))
        if self.s3_p1_r4.isChecked():
            secre = secret.secr(li, lev, 12)
            secre = secre + secret.secr(li, lev, 13)
            secre = secre + secret.secr(li, lev, 14)
            secre = secre + secret.secr(li, lev, 15)
            secre = secre + secret.secr(li, lev, 16)
            self.s3_p2_t1.setText('\n'.join(secre))
            
    def on_s3_p2_b1_clicked(self):
        self.stackedWidget_3.setCurrentIndex(0)
        
    @pyqtSlot()
    def on_b5_clicked(self):
        self.stackedWidget.setCurrentIndex(4)
        
    @pyqtSlot()
    def on_b6_clicked(self):
        self.stackedWidget.setCurrentIndex(5)
        
    @pyqtSlot()
    def on_b7_clicked(self):
        self.stackedWidget.setCurrentIndex(6)
        
    @pyqtSlot()
    def on_b8_clicked(self):
        self.stackedWidget.setCurrentIndex(7)
        
    @pyqtSlot()
    def on_b9_clicked(self):
        self.stackedWidget.setCurrentIndex(8)
        
    @pyqtSlot()
    def on_b10_clicked(self):
        self.stackedWidget.setCurrentIndex(9)
        
    @pyqtSlot()
    def on_b11_clicked(self):
        self.stackedWidget.setCurrentIndex(10)
        
    @pyqtSlot()
    def on_b12_clicked(self):
        self.stackedWidget.setCurrentIndex(11)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    switch = switch()
    switch.show()
    sys.exit(app.exec_())
