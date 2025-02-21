#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict

from backend.core.path_conf import BasePath


class OssSettings(BaseSettings):
    """xxx Settings"""

    model_config = SettingsConfigDict(env_file=f'{BasePath}/.env', env_file_encoding='utf-8', extra='ignore')

    # Env oss
    OSS_ACCESS_KEY: str
    OSS_SECRET_KEY: str

    # Oss
    OSS_BUCKET_NAME: str = 'fba-test'
    OSS_ENDPOINT: str = 'https://oss-cn-hangzhou.aliyuncs.com'


@lru_cache
def get_oss_settings() -> OssSettings:
    """获取 xxx 配置"""
    return OssSettings()


oss_settings = get_oss_settings()
