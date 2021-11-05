from django.shortcuts import render, redirect
import requests
import time
import psutil
import os
from datetime import datetime
from .models import Monitor
from urllib.parse import urlparse
from django.core.paginator import Paginator