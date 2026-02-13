# op_ace6_kbuild

Oneplus ACE6 内核构建脚本，可以集成KernelSU及其变体 也包括SUSFS的集成

## 仓库简介

本仓库提供一套基于 GitHub Actions 的自动化构建脚本套件，用于编译一加 ACE6 内核，内置 KernelSU 与 SUSFS 功能集成支持。

仓库包含 GitHub Actions 工作流文件及预编译辅助工具，不包含任何 OEM 内核源码 —— 内核源码需从 OEM 官方渠道另行获取。

预编译工具 `scripts/configure` 作为构建阶段辅助程序，具备以下核心能力：

- 仅在开启特定功能（KPM）时，自动修改 `arch/arm64/Makefile` 并打补丁，确保最终生成的内核镜像按需集成目标功能。
- 内置严格的白名单与黑名单校验机制：白名单用户可无限制启用所有受限功能，黑名单用户则会被直接阻止整个构建流程。

## 使用方法 

1. Fork 本仓库

2. 启用Action ，并在build custom工作流中根据需求调整相关参数

3. 坐等放宽，等待构建完成

4. 从 Actions 制品中下载编译完成的内核镜像，并刷入，大功告成

## 许可证声明

|组件|许可证|详情|
|--|--|--|
|GitHub Actions 工作流|MIT 许可证|详见根目录 LICENSE 文件|
|预编译二进制文件 (`scripts/configure`)|BSD 2-Clause 许可证|详见根目录 LICENSE-scripts-configure 文件|
|OEM 内核源码|GPLv2 许可证|遵守 OEM 内核的原始许可条款 |

## 重要说明

1. `scripts/configure` 为独立的构建阶段辅助工具，仅在构建过程中开启特定功能时修改内核构建配置文件，不参与内核编译链接，也不会嵌入最终的内核镜像。

2. `scripts/configure` 的修改行为不会影响 OEM 内核源码的 GPLv2 许可属性。

3. 分发本仓库时，必须保留原始版权声明与许可证文本；分发编译后的内核包时，仅需遵守 OEM 内核的 GPLv2 条款，无需附带本仓库的许可信息。

4. 维护者保留通过 `scripts/configure` 内置的黑白名单机制进行访问控制的权利，该限制不违反 BSD 2-Clause 许可证条款。
