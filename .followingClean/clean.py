o
    s�b�  �                   @   s�   d dl Z d dlZd dlZd dlZzd dlZW n   e �d� d dlZY dZdZdZdZ	dZ
dZdZd	Zd
ZdZe �d� dd� Zdd� Zdd� Zz	e�  e�  W dS  ey`   e��  Y dS w )�    Nzpip install requestsz[94mz[91mz[97mz[93mz[1;32mz[96mz[0mz[0;35mz

 https://bit.ly/3Hz6Ff5�clearc                   C   s,   t �d� t �d� t �d� t �d� d S )N�..zlolcat banner.shz.Textzlolcat MyText.txt)�os�chdir�system� r   r   �clean.py�header"   s   


r	   c                 C   s2   | d D ]}t j�|� t j��  t�d� qd S )N�
g���Q��?)�sys�stdout�write�flush�time�sleep)�zZwordr   r   r   �	logoprint)   s
   
�r   c                  C   s�  	 t �d� ttd t �} | dk�r�d|  d }ddlm} |� }d	|d
< d|d< d|d< d|d< tj||d�}t �d� t	�  t
td � t�d� t �d� t	�  t
td t |  � t
td t |�� d d  d � t�d� |�� d d }d}tt|��D ]3}t
td t |�� d d | d  t d t d |�� d d | d  � t�d � |d!  q�	 tttd" ��}|d#ks�|d$k�r�t �d� t	�  t �d%� tttd& t ��}t�d'� t �d� t	�  ttd( � t�d� d)t d* }	ddlm} |� }||d
< d|d< d|d< d|d< tj|	|d�}
|�� d d }d}tt|��D ]o}|�� d d | d }t�d+� ddlm} d,| d- }ddlm} |� }||d
< d|d< d|d< d|d< z'tj||d�}|�� d. }|d/k�r�ttd0 t | t d1 � t�d� W n
   t
td2 � Y |d!  �q0ntttd3 ��}|dk�r�t��  nt
td4 � q�nt
td5 � qtttd6 t ��}|dk�r�t �d7� t �d8� t �d9� t�d� d S t��  d S ):NTzlolcat clean.shz
     Enter Circle ID: � z_https://circle.robi.com.bd/mylife/appapi/appcall.php?op=getFollowingInfoList&offset=0&nickname=z
&limit=500r   )�CaseInsensitiveDictZ d29ac47b3ce9de73bb99c1b98dd6159bz	x-api-keyZ(000oc0so48owkw4s0wwo4c00g00804w80gwkw8kgz	x-app-key�gzipz
User-Agentz!application/x-www-form-urlencodedzContent-Type)�headersr   z%

     Your Following Data Loading...�   z
     Your ID: z     Total Following: �data�totalr
   Z	followingz
 Nickname: �nicknamez
  Number: �+Zmsisdng�������?�   z.
 Are you sure clean your following list y/n? �Y�yzlolcat clean.goz     Enter Your API Key: �   z$

     Your Request In Prossesing...z�https://circle.robi.com.bd/mylife/appapi/appcall.php?op=performAction&app_version=81&action=kast&msgId=62&message=Hey!+I'm+Cleaning+My+Following+List+From+ARU's+System.z&retry=false�   zYhttps://circle.robi.com.bd/mylife/appapi/appcall.php?op=stopFren&app_version=81&nickname=zM&msgId=71&imei=355176100129757&imsi=470022500179917&retry=false&operator=RobiZrdesczRequest acceptedz

      You have left zV's circle & will not 
     be receiving his/her status update 
        CSHOUT anymore.z
    Error z
     Press Enter To Exit z
     You Enterd Invalid Valuez
     Please Enter Valid IDz"

     Press Enter For Again Find r   z.showFollowingszpython followings.py)r   r   �input�green�yellowZrequests.structuresr   �requests�getr	   �printr   r   �json�range�len�cyan�str�whiter   �mark�redr   �exit�purpler   )�userZurlr   r   Zrespr   �iZsureZapiZurl1�str   Z
url_removeZrespsZ	returnValr/   Zenterr   r   r   �main0   s�   




$
P









�
�7�Y



r4   )r   r   r'   r   r$   r   ZblueZ	lightbluer.   r,   r#   r"   r*   �endr0   r-   r	   r   r4   �KeyboardInterruptr/   r   r   r   r   �<module>   s4    


d�