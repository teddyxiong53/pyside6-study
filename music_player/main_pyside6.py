#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QSlider
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtCore import Qt
import os
import sys

class MusicPlayerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("音乐播放器")
        self.resize(1024, 768)
        
        # 主窗口设置
        self.setStyleSheet("background-color: white;")
        
        # 创建主部件
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        
        # 主布局
        self.main_layout = QVBoxLayout()
        self.main_widget.setLayout(self.main_layout)
        
        # 创建顶部面板
        self.create_top_panel()
        
        # 创建内容面板
        self.create_content_panel()
        
        # 创建底部播放控制面板
        self.create_player_controls()
        
        # 添加面板到主布局
        self.main_layout.addWidget(self.top_panel)
        self.main_layout.addWidget(self.content_panel)
        self.main_layout.addWidget(self.player_panel)
    
    def create_top_panel(self):
        """创建顶部面板"""
        self.top_panel = QWidget()
        self.top_panel.setStyleSheet("background-color: white;")
        top_layout = QHBoxLayout(self.top_panel)
        
        # 用户信息区域
        user_widget = QWidget()
        user_layout = QHBoxLayout(user_widget)
        
        # 用户头像
        avatar = QLabel()
        avatar.setPixmap(QPixmap(50, 50))
        
        # 用户信息
        user_info = QVBoxLayout()
        user_name = QLabel("Farzan Faruk")
        user_name.setFont(QFont("Arial", 12, QFont.Bold))
        user_email = QLabel("Loova.studio@gmail.com")
        user_email.setStyleSheet("color: #787878;")
        
        user_info.addWidget(user_name)
        user_info.addWidget(user_email)
        
        user_layout.addWidget(avatar)
        user_layout.addLayout(user_info)
        
        # 搜索栏
        search_widget = QWidget()
        search_layout = QHBoxLayout(search_widget)
        search_bar = QLineEdit()
        search_bar.setPlaceholderText("Search for song, artists etc...")
        search_layout.addWidget(search_bar)
        
        # 右侧按钮
        buttons_widget = QWidget()
        buttons_layout = QHBoxLayout(buttons_widget)
        settings_btn = QPushButton("⚙️")
        upgrade_btn = QPushButton("Upgrade Pro")
        upgrade_btn.setStyleSheet("background-color: #ff3232; color: white;")
        
        buttons_layout.addWidget(settings_btn)
        buttons_layout.addWidget(upgrade_btn)
        
        # 添加到顶部布局
        top_layout.addWidget(user_widget)
        top_layout.addWidget(search_widget, stretch=1)
        top_layout.addWidget(buttons_widget)
    
    def create_content_panel(self):
        """创建内容面板"""
        self.content_panel = QWidget()
        content_layout = QHBoxLayout(self.content_panel)
        
        # 创建侧边栏
        self.create_sidebar()
        
        # 创建主内容区
        self.create_main_content()
        
        content_layout.addWidget(self.sidebar_panel)
        content_layout.addWidget(self.main_content_panel, stretch=1)
    
    def create_sidebar(self):
        """创建侧边栏"""
        self.sidebar_panel = QWidget()
        self.sidebar_panel.setStyleSheet("background-color: #fafafa;")
        sidebar_layout = QVBoxLayout(self.sidebar_panel)
        
        # 导航菜单
        nav_items = ["🏠 Home", "🔍 Browse", "💿 Album", "👤 Artists", "🎬 Videos"]
        for i, item in enumerate(nav_items):
            btn = QPushButton(item)
            btn.setStyleSheet("text-align: left; padding: 10px;")
            if i == 0:
                btn.setStyleSheet("background-color: #f0f0ff; color: #0000c8; text-align: left; padding: 10px;")
            sidebar_layout.addWidget(btn)
        
        # 我的音乐
        sidebar_layout.addWidget(QLabel("MY MUSIC"))
        my_music_items = ["🕒 Recently Played", "📁 Local Files"]
        for item in my_music_items:
            btn = QPushButton(item)
            btn.setStyleSheet("text-align: left; padding: 10px;")
            sidebar_layout.addWidget(btn)
        
        # 设备信息
        device_widget = QWidget()
        device_widget.setStyleSheet("background-color: #f0f0f0;")
        device_layout = QHBoxLayout(device_widget)
        
        device_icon = QLabel("📱")
        device_info = QVBoxLayout()
        device_name = QLabel("iPhone X")
        device_storage = QLabel("128 GB")
        device_storage.setStyleSheet("color: #787878;")
        
        device_info.addWidget(device_name)
        device_info.addWidget(device_storage)
        
        device_layout.addWidget(device_icon)
        device_layout.addLayout(device_info)
        
        sidebar_layout.addWidget(device_widget)
    
    def create_main_content(self):
        """创建主内容区"""
        self.main_content_panel = QWidget()
        main_content_layout = QVBoxLayout(self.main_content_panel)
        
        # Billboard Topchart
        topchart_widget = QWidget()
        topchart_layout = QVBoxLayout(topchart_widget)
        
        # 标题和导航
        title_bar = QWidget()
        title_layout = QHBoxLayout(title_bar)
        title = QLabel("Billboard Topchart")
        title.setFont(QFont("Arial", 16, QFont.Bold))
        
        nav_buttons = QHBoxLayout()
        prev_btn = QPushButton("<")
        next_btn = QPushButton(">")
        
        nav_buttons.addWidget(prev_btn)
        nav_buttons.addWidget(next_btn)
        
        title_layout.addWidget(title, stretch=1)
        title_layout.addLayout(nav_buttons)
        
        # 专辑封面
        albums_widget = QWidget()
        albums_layout = QHBoxLayout(albums_widget)
        
        album_titles = ["Coloring Book", "Blue Neighbourhood", "Starboy", "Mirage", "Beerbongs"]
        album_artists = ["Chance The Rapper", "Troye Sivan", "The Weeknd", "Else Twin", "Post Malone"]
        
        for title, artist in zip(album_titles, album_artists):
            album_widget = QWidget()
            album_layout = QVBoxLayout(album_widget)
            
            cover = QLabel()
            cover.setPixmap(QPixmap(150, 150))
            
            album_title = QLabel(title)
            album_artist = QLabel(artist)
            album_artist.setStyleSheet("color: #787878;")
            
            album_layout.addWidget(cover)
            album_layout.addWidget(album_title)
            album_layout.addWidget(album_artist)
            
            albums_layout.addWidget(album_widget)
        
        topchart_layout.addWidget(title_bar)
        topchart_layout.addWidget(albums_widget)
        
        # 播放列表
        playlists_widget = QWidget()
        playlists_layout = QHBoxLayout(playlists_widget)
        
        # 热门歌曲
        popular_widget = QWidget()
        popular_layout = QVBoxLayout(popular_widget)
        
        popular_title = QLabel("Most Popular")
        popular_title.setFont(QFont("Arial", 16, QFont.Bold))
        popular_count = QLabel("16 songs")
        popular_count.setStyleSheet("color: #787878;")
        
        popular_header = QHBoxLayout()
        popular_header.addWidget(popular_title)
        popular_header.addWidget(popular_count)
        
        # 歌曲列表
        songs_widget = QWidget()
        songs_layout = QVBoxLayout(songs_widget)
        
        song_titles = ["My Stress", "Mirage", "My Stress", "The Hills", "Paralyzed", "Timeless"]
        song_artists = ["NF Real music", "Else Twin", "NF Real music", "The Weeknd", "NF Real music", "Lucidious"]
        song_times = ["3:22", "4:23", "3:58", "5:33", "5:06", "3:50"]
        
        for i, (title, artist, time) in enumerate(zip(song_titles, song_artists, song_times)):
            song_widget = QWidget()
            song_widget.setStyleSheet("background-color: #fafafa;" if i % 2 == 0 else "background-color: white;")
            song_layout = QHBoxLayout(song_widget)
            
            index = QLabel(f"{i+1:02d}")
            index.setStyleSheet("color: #787878;")
            
            cover = QLabel()
            cover.setPixmap(QPixmap(40, 40))
            
            song_info = QVBoxLayout()
            song_title = QLabel(title)
            song_artist = QLabel(artist)
            song_artist.setStyleSheet("color: #787878;")
            
            song_info.addWidget(song_title)
            song_info.addWidget(song_artist)
            
            duration = QLabel(time)
            duration.setStyleSheet("color: #787878;")
            
            like_btn = QPushButton("❤️")
            if i % 2 == 0:
                like_btn.setStyleSheet("color: red;")
            else:
                like_btn.setStyleSheet("color: #c8c8c8;")
            
            song_layout.addWidget(index)
            song_layout.addWidget(cover)
            song_layout.addLayout(song_info)
            song_layout.addWidget(duration)
            song_layout.addWidget(like_btn)
            
            songs_layout.addWidget(song_widget)
        
        popular_layout.addLayout(popular_header)
        popular_layout.addWidget(songs_widget)
        
        # 正在播放
        now_playing_widget = QWidget()
        now_playing_layout = QVBoxLayout(now_playing_widget)
        
        now_playing_title = QLabel("Now Playing")
        now_playing_title.setFont(QFont("Arial", 16, QFont.Bold))
        now_playing_count = QLabel("65 items on the list")
        now_playing_count.setStyleSheet("color: #787878;")
        
        now_playing_header = QHBoxLayout()
        now_playing_header.addWidget(now_playing_title)
        now_playing_header.addWidget(now_playing_count)
        
        # 当前播放歌曲
        current_song_widget = QWidget()
        current_song_widget.setStyleSheet("background-color: #fafafa;")
        current_song_layout = QVBoxLayout(current_song_widget)
        
        cover = QLabel()
        cover.setPixmap(QPixmap(150, 150))
        
        song_info = QLabel("Chance The Rapper")
        song_info.setFont(QFont("Arial", 12, QFont.Bold))
        
        # 进度条
        progress_widget = QWidget()
        progress_layout = QVBoxLayout(progress_widget)
        
        slider = QSlider(Qt.Horizontal)
        slider.setValue(30)
        
        time_layout = QHBoxLayout()
        current_time = QLabel("2:10")
        current_time.setStyleSheet("color: #787878;")
        total_time = QLabel("-03:36")
        total_time.setStyleSheet("color: #787878;")
        
        time_layout.addWidget(current_time)
        time_layout.addStretch()
        time_layout.addWidget(total_time)
        
        progress_layout.addWidget(slider)
        progress_layout.addLayout(time_layout)
        
        # 控制按钮
        controls_widget = QWidget()
        controls_layout = QHBoxLayout(controls_widget)
        
        shuffle_btn = QPushButton("🔀")
        prev_btn = QPushButton("⏮")
        play_btn = QPushButton("⏸")
        next_btn = QPushButton("⏭")
        repeat_btn = QPushButton("🔁")
        
        controls_layout.addStretch()
        controls_layout.addWidget(shuffle_btn)
        controls_layout.addWidget(prev_btn)
        controls_layout.addWidget(play_btn)
        controls_layout.addWidget(next_btn)
        controls_layout.addWidget(repeat_btn)
        controls_layout.addStretch()
        
        current_song_layout.addWidget(cover, 0, Qt.AlignCenter)
        current_song_layout.addWidget(song_info, 0, Qt.AlignCenter)
        current_song_layout.addWidget(progress_widget)
        current_song_layout.addWidget(controls_widget)
        
        now_playing_layout.addLayout(now_playing_header)
        now_playing_layout.addWidget(current_song_widget)
        
        playlists_layout.addWidget(popular_widget, stretch=1)
        playlists_layout.addWidget(now_playing_widget, stretch=1)
        
        main_content_layout.addWidget(topchart_widget)
        main_content_layout.addWidget(playlists_widget, stretch=1)
    
    def create_player_controls(self):
        """创建底部播放控制面板"""
        self.player_panel = QWidget()
        self.player_panel.setStyleSheet("background-color: #f5f5f5;")
        player_layout = QHBoxLayout(self.player_panel)
        
        # 这里可以添加底部播放控制器的UI元素
        # 但在原代码中看不到底部控制器，所以这里留空

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MusicPlayerWindow()
    window.show()
    sys.exit(app.exec())