o
    �by  �                   @   s�   d dl Z d dlZd dlZd dlZzd dlZW n   e �d� d dlZY dZdZdZdZ	dZ
dZdZd	Zd
Ze �d� dd� Zdd� Zdd� Zz	e�  e�  W dS  ey^   e��  Y dS w )�    Nzpip install requestsz[94mz[91mz[97mz[93mz[1;32mz[96mz[0mz[0;35m�clearc                   C   s,   t �d� t �d� t �d� t �d� d S )N�..zlolcat banner.shz.Textzlolcat MyText.txt)�os�chdir�system� r   r   �
showBlk.py�header   s   


r	   c                 C   s2   | d D ]}t j�|� t j��  t�d� qd S )N�
g���Q��?)�sys�stdout�write�flush�time�sleep)�zZwordr   r   r   �	logoprint%   s
   
�r   c                  C   s�  	 t td t �} | dkr�d}d}ddlm} |� }| |d< d	|d
< d|d< d|d< tj|||d�}t�d� t	�  t
td � t�d� t�d� t	�  |�� d }d|vrat
td � t��  |�� d d }t
td t |  � t
td t t|� d � t�d� |�� d d }d}	g }
tt|��D ]D}	t
td t |�� d d |	 d  t d t d |�� d d |	 d  � |�� d d |	 d }|
�|� t�d� |	d   q�nt
td! � qtt td" t ��}|�� }|dk�rJt�d� t	�  |
D ]E}d}d#| }z
tj|||d�}W n
   t
td$ � Y |�� d% }|d&k�r;ttd' t | � t�d � �qttd( � t�d)� �qd S |d*k�r[t�d+� t�d,� d S t��  d S )-NTz
     Enter API Key: � z5https://circle.robi.com.bd/mylife/appapi/appcall.php?zop=getBlockedUserInfoListr   )�CaseInsensitiveDictz	x-api-keyZ(000oc0so48owkw4s0wwo4c00g00804w80gwkw8kgz	x-app-key�gzipz
User-Agentz!application/x-www-form-urlencodedzContent-Type)�headers�datar   z$

     Your Bloacked Data Loading...�   r   �listz
   Blocked Account Not Found�totalz
     Your API Key: z
     Total Blocked: r
   z
 Nickname: Znicknamez
  Number: �+Zmsisdng�������?�   z 
     Please Enter Valid API Keyz$

     Press Enter For Unblock All  zop=unblockUser&nickname=z     No internetZrdescZOKz
     Successfully unblocked z   Your API Key Maybe Invalid�   �mr   zpython circle.py)�input�green�yellowZrequests.structuresr   �requestsZpostr   r   r	   �printr   r   �json�redr   �exit�str�range�len�cyan�append�purple�lowerr   r   )�keyZurlr   r   r   Zrespr   Ztotal_blked�y�iZlistBlockedZnickZenter�x�statusr   r   r   �main,   sz   



P


�0


�

r3   )r   r   r$   r   r"   r   ZblueZ	lightbluer%   Zwhiter!   r    r*   �endr,   r	   r   r3   �KeyboardInterruptr&   r   r   r   r   �<module>   s2    



K�