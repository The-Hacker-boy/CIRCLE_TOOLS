o
    0��b�  �                   @   s�   d dl Z d dlZd dlZd dlZzd dlZW n   e �d� d dlZY dZdZdZdZ	dZ
dZdZd	Zd
Ze �d� dd� Zdd� Zdd� Zze�  W dS  ey[   e��  Y dS w )�    Nzpip install requestsz[94mz[91mz[97mz[93mz[1;32mz[96mz[0mz[0;35m�clearc                   C   s,   t �d� t �d� t �d� t �d� d S )N�..zlolcat banner.shz.Textzlolcat MyText.txt)�os�chdir�system� r   r   �updateApp.py�header   s   


r	   c                 C   s2   | d D ]}t j�|� t j��  t�d� qd S )N�
g���Q��?)�sys�stdout�write�flush�time�sleep)�zZwordr   r   r   �	logoprint%   s
   
�r   c                  C   s�  	 d} ddl m} |� }d|d< d|d< d	|d
< d|d< tj| |d�}t�d� t�  ttd � t	�
d� t�d� t�  ttd � t	�
d� |�� d d }d}tt|��D ]E}ttd t |�� d d | d  t d t d |�� d d | d  t d t |�� d d | d  � t	�
d� |d  qY	 tttd t ��}|dkr�t�d � t�d!� t�d"� t	�
d� d S t��  d S )#NTz�https://circle.robi.com.bd/mylife/appapi/appcall.php?op=getLatestBommList&lkey=d29ac47b3ce9de73bb99c1b98dd6159b8801894747699&msisdn=8801894747699r   )�CaseInsensitiveDictZ d29ac47b3ce9de73bb99c1b98dd6159bz	x-api-keyZ(000oc0so48owkw4s0wwo4c00g00804w80gwkw8kgz	x-app-key�gzipz
User-Agentz!application/x-www-form-urlencodedzContent-Type)�headersr   z-

     The Latest Updated Data is Loading ...�   z#
     The Latest Update In apps... �   �dataZmlstatus_itemz

Name: Znicknamez	
Number: �+Zmsisdnz
Shout: Zmlstatusg333333�?�   z'

     Press Enter For Chek New Update � r   z.updatezpython updateApp.py)Zrequests.structuresr   �requests�getr   r   r	   �print�greenr   r   �json�range�len�yellow�white�cyan�str�input�purpler   r   �exit)Zurlr   r   Zresp�y�iZenterr   r   r   �main,   s>   



t




r,   )r   r   r    r   r   r   ZblueZ	lightblueZredr$   r#   r   r%   �endr(   r	   r   r,   �KeyboardInterruptr)   r   r   r   r   �<module>   s0    



&�