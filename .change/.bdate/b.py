o
    ���b�	  �                   @   s�   d dl Z d dlZzd dlZW n   e �d� d dlZY dZdZdZdZdZdZ	dZ
d	Zd
ZdZe �d� dd� Zdd� Zdd� Zdd� Zz	e�  e�  W dS  ey\   e��  Y dS w )�    Nzpip install requestsz[94mz[91mz[97mz[93mz[1;32mz[96mz[0mz[0;35mz

 https://bit.ly/3Hz6Ff5�clearc                   C   s6   t �d� t �d� t �d� t �d� t �d� d S �N�..zlolcat banner.shz.Textzlolcat MyText.txt��os�chdir�system� r	   r	   �b.py�header    s
   



r   c                   C   s,   t �d� t �d� t �d� t �d� d S r   r   r	   r	   r	   r
   �header2&   s   


r   c                 C   s2   | d D ]}t j�|� t j��  t�d� qd S )N�
g���Q��?)�sys�stdout�write�flush�time�sleep)�zZwordr	   r	   r
   �	logoprint+   s
   
�r   c                  C   sf  t �d� tttd t ��} t �d� t�  tttd t ��}ddlm} d| }ddlm} |� }| |d< d	|d
< d|d< d|d< z7t	j
||d�}|�� d d }|dkrtttd t | t d � dt d }t	j
||d�}nttd � W n   td� Y tttd t ��}|dkr�t �d� t �d� t �d� t �d� t�d� d S t��  d S ) Nzlolcat b.shz     Enter API Key: r   z'

  Enter Your Birthday [YYYY-MM-DD] : r   )�CaseInsensitiveDictzMhttps://circle.robi.com.bd/mylife/appapi/appcall.php?op=setUserInfo&birthday=z	x-api-keyZ(000oc0so48owkw4s0wwo4c00g00804w80gwkw8kgz	x-app-key�gzipz
User-Agentz!application/x-www-form-urlencodedzContent-Type)�headers�data�updated�   z
     Your Birthday: z

     Succesfully Udadtedz�https://circle.robi.com.bd/mylife/appapi/appcall.php?op=performAction&app_version=81&action=kast&msgId=62&message=Hey!+I'm+Change+My+Birthday+From+ARU's+System.z&retry=falsez

     Error z=
     Your Request Rejected.Please Use VPN or Try Again Leterz$

     Press Enter For Again Change � r   z.changez.bdatezpython b.py�   )r   r   �str�input�green�yellowr   Zrequests.structuresr   �requests�getZjson�print�cyan�mark�red�purpler   r   r   r   �exit)ZapiZbirthdayr   Zurlr   Zresp�statusZenterr	   r	   r
   �main0   s@   

�




r+   )r   r   r"   r   ZblueZ	lightbluer'   Zwhiter!   r    r%   �endr(   r&   r   r   r   r+   �KeyboardInterruptr)   r	   r	   r	   r
   �<module>   s6   


$�