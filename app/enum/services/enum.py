import core.pentests.enum as enumCore
import socket
class EnumService:
    def __init__(self):
        ...

    @staticmethod
    async def dns_lookup(domain_name:str) -> str:
        try:
            return enumCore.dns_lookup(domain_name)
        except socket.gaierror:
            return None
   
    @staticmethod
    async def dns_reverse_lookup(ip_address:str) -> str:
        try:
            return enumCore.reverse_dns_lookup(ip_address)
        except socket.herror:
            return None
        
    @staticmethod
    async def smtp_users(mail_server:str, port:int) -> str:
        try:
            return enumCore.get_smtp_users(mail_server, port)
        except:
            return None
    
    async def zone_transfer(mail_server:str) -> str:
        try:
            return enumCore.zone_transfer(mail_server)
        except:
            return []
    
    @staticmethod
    async def dns_records(domain_name:str) -> str:
        return enumCore.get_dns_records(domain_name)
        
        
