#!/bin/bash

# 设定环境变量名称
ENV_VAR_NAME="TEST_ENV"

# 获取环境变量的值
ENV_VAR_VALUE=$(printenv $ENV_VAR_NAME)

# 验证环境变量的值
if [ "$ENV_VAR_VALUE" == "123" ]; then
  echo "环境变量 $ENV_VAR_NAME 的值正确。"
  exit 0  # 返回码 0，表示成功
else
  echo "环境变量 $ENV_VAR_NAME 的值不符合预期。"
  exit 1  # 返回码 1，表示失败
fi

