import sys
from direct.showbase.ShowBase import ShowBase
from direct.directnotify import DirectNotifyGlobal

from src.util.LogManager import LogManager
from src.core.ConnectionManager import ConnectionManager
from src.message.MessageManager import MessageManager


class ServerBase(ShowBase):
    notify = DirectNotifyGlobal.directNotify.newCategory("ServerBase")
    serverVersion = 'pcsv1.0.34.31'

    def __init__(self):
        ShowBase.__init__(self)

        self.activeConnections = {}

        self.configManager = None

        self.logManager = LogManager()
        self.connectionManager = ConnectionManager()
        self.messageManager = MessageManager()