# U+32C3C · 中日韩统一表意文字扩展J区
# CJK Unified Ideograph Extension J · Unicode 17.0

此字符收录于 Unicode 17.0 第三表意文字平面扩展J区，目前尚未被大多数系统字体支持。本项目提供完整的跨平台安装包。

*This character is part of Unicode 17.0 CJK Extension J on the Tertiary Ideographic Plane. Most system fonts do not yet support it. This package provides full cross-platform installation.*

---

## 文件说明 · Files

| 文件 | 用途 |
|---|---|
| `index.html` | 在线字形书写器（用浏览器打开）|
| `NotoSansCJKsc-Patched.otf` | macOS / Windows 字体文件 |
| `subset.otf` | 浏览器用单字形子集字体 |
| `font-profile.mobileconfig` | iOS 字体配置文件 |
| `u32c3c.user.css` | Stylus 一键安装样式 |

---

## macOS 安装 · macOS Installation

1. 双击 `NotoSansCJKsc-Patched.otf`
2. 点击「安装字体」
3. 在 Sublime Text、TextEdit、Pages 等应用中选择字体 **Noto Sans CJK SC Patched** 即可使用

*Double-click `NotoSansCJKsc-Patched.otf` and click Install Font. Select Noto Sans CJK SC Patched in any app.*

---

## Windows 安装 · Windows Installation

1. 右键点击 `NotoSansCJKsc-Patched.otf`
2. 选择「为所有用户安装」（推荐）或「安装」
3. 在 Word、Notepad、Sublime Text 等应用中选择字体 **Noto Sans CJK SC Patched** 即可使用

*Right-click `NotoSansCJKsc-Patched.otf` and select Install for all users. Select Noto Sans CJK SC Patched in any app.*

---

## iOS 安装 · iOS Installation

1. 将 `font-profile.mobileconfig` AirDrop 至 iPhone
2. 前往「设置」→ 顶部「已下载描述文件」→「安装」
3. 在 Pages / Keynote / Word 中选择字体使用

*AirDrop `font-profile.mobileconfig` to iPhone. Go to Settings → Profile Downloaded → Install.*

---

## 浏览器安装 · Browser Installation

1. 安装 [Stylus 扩展](https://chrome.google.com/webstore/detail/stylus/clngdbkpkpeebahjckkjfobafhncgmne)（Chrome / Firefox / Arc）
2. 将 `subset.otf` 上传至任意静态托管服务（如 Netlify）
3. 修改 `u32c3c.user.css` 中的 URL 为你的托管地址
4. 点击 `u32c3c.user.css`，Stylus 自动弹出安装确认

或直接访问发布页，点击「一键安装 Stylus 样式」按钮。

*Install the Stylus extension, host subset.otf, update the URL in u32c3c.user.css, then click the file to trigger one-click install.*

---

## 文字替换快捷输入 · Text Replacement Shortcut

**macOS / iOS（自动 iCloud 同步）：**

1. 「系统设置 → 键盘 → 文字替换」→「+」
2. 「替换为」粘贴字符，「快捷键」填写拼音（如 `u32c3c`）

*System Settings → Keyboard → Text Replacement → + → paste character in Phrase, type shortcut.*

---

## 字体授权 · License

字体基于 **Noto Sans CJK**，遵循 [SIL Open Font License 1.1](https://scripts.sil.org/OFL)。
可自由使用、修改与再分发，但须保留原授权声明。

*Based on Noto Sans CJK, licensed under SIL OFL 1.1. Free to use, modify and redistribute with attribution.*
