o
    ���b[  �                   @   s�   d dl Z d dlZd dlZd dlZzd dlZW n   e �d� d dlZY dZdZdZdZ	dZ
dZdZd	Zd
Ze �d� dd� Zdd� Zdd� Zz	e�  e�  W dS  ey^   e��  Y dS w )�    Nzpip install requestsz[94mz[91mz[97mz[93mz[1;32mz[96mz[0mz[0;35m�clearc                   C   s,   t �d� t �d� t �d� t �d� d S )N�..zlolcat banner.shz.Textzlolcat MyText.txt)�os�chdir�system� r   r   �shout.py�header   s   


r	   c                 C   s2   | d D ]}t j�|� t j��  t�d� qd S )N�
g���Q��?)�sys�stdout�write�flush�time�sleep)�zZwordr   r   r   �	logoprint%   s
   
�r   c                  C   sr  	 t ttd t ��} | dkr�d|  }ddlm} |� }d|d< d	|d
< d|d< d|d< tj||d�}t�	d� t
�  ttd � t�d� t�	d� t
�  ttd t |  � t�d� |�� d }d}tt|��D ]}tdt |�� d | d  � t�d� |d  qknttd � qt ttd t ��}|dkr�t�d� t�d� t�	d� t�d� d S t��  d S )NTz
     Enter Circle ID: � zQhttps://circle.robi.com.bd/mylife/appapi/appcall.php?op=getMLStatusList&nickname=r   )�CaseInsensitiveDictZ d29ac47b3ce9de73bb99c1b98dd6159bz	x-api-keyZ(000oc0so48owkw4s0wwo4c00g00804w80gwkw8kgz	x-app-key�gzipz
User-Agentz!application/x-www-form-urlencodedzContent-Type)�headersr   z

     Your Shout Loading...�   z
     Your ID: �   �dataz

   �stg333333�?�   z
     Please Enter Valid IDz"

     Press Enter For Again Find r   z.updatezpython shout.py)�str�input�green�yellowZrequests.structuresr   �requests�getr   r   r	   �printr   r   �json�range�len�red�purpler   r   �exit)�userZurlr   r   Zresp�y�iZenterr   r   r   �main,   sF   



 

� 


r,   )r   r   r#   r   r    r   ZblueZ	lightbluer&   Zwhiter   r   Zcyan�endr'   r	   r   r,   �KeyboardInterruptr(   r   r   r   r   �<module>   s2    



+�