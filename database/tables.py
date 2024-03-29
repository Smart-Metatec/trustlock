from msilib import Table
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from enum import Enum

from utils.encryption import Encryption

class TableEnum(Enum):
    apps = 'apps'
    notes = 'notes'
    todos = 'todos'
    settings = 'settings'
    users = 'users'
    vault = 'vault'
    metadata = 'metadata'
    groups = 'groups'
    

class Tables:
    def __init__(self, key) -> None:
        self.enc = Encryption(key).encrypt
    
    def tables(self) -> dict[TableEnum, dict[str, str]]:
        
        apps = {
            "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
            "name": "TEXT NOT NULL",
            "path": "TEXT NOT NULL",
            "sequence": "INTEGER NOT NULL",
            "group_id": "INTEGER",
        }
        
        notes = {
            "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
            "name": "TEXT NOT NULL",
            "body": "TEXT",
            "group_id": "INTEGER",
        }
        
        todos = {
            "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
            "name": "TEXT NOT NULL",
            "complete": f"TEXT DEFAULT '{self.enc('0')}' NOT NULL",
            "deadline": "TEXT",
            "description": "TEXT",
            "group_id": "INTEGER",
        }
        
        settings = {
            "id": f"TEXT PRIMARY KEY",
            "nightmode": f"TEXT NOT NULL",
            "font": f"TEXT NOT NULL",
            "color": f"TEXT NOT NULL",
            "vault_on": f"TEXT NOT NULL",
            "timer": f"TEXT NOT NULL",
            "calendar": f"TEXT NOT NULL",
            "twofa": f"TEXT",
            "auto_save": f"TEXT"
        }
        
        users = {
            "id": f"TEXT DEFAULT '{self.enc('user')}' PRIMARY KEY",
            "name": "TEXT NOT NULL",
            "email": "TEXT NOT NULL",
            "password": "TEXT NOT NULL",
            "passphrase": "TEXT NOT NULL",
            "twofa_key": "TEXT",
            "password_exp": "TEXT"
        }
        
        vault = {
            "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
            "type": "TEXT NOT NULL",
            "name": "TEXT NOT NULL",
            "data": "TEXT NOT NULL",
            "group_id": "INTEGER",
        }
        
        metadata = {
            "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
            "name": "TEXT NOT NULL",
            "data": "TEXT NOT NULL"
        }
        
        groups = {
            "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
            "name": "TEXT NOT NULL",
            "description": "TEXT NOT NULL"
        }
        
        return {
            TableEnum.apps: apps,
            TableEnum.notes: notes,
            TableEnum.todos: todos,
            TableEnum.settings: settings,
            TableEnum.users: users,
            TableEnum.vault: vault,
            TableEnum.metadata: metadata,
            TableEnum.groups: groups
        }