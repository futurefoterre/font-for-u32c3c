## 5/8/2026 更新
5/8/2026 Update

新增字符“𢗼” U+225FC

Added unicode character U+225FC

---

# 𲰼 U+32C3C · 中日韩统一表意文字扩展J区
# CJK Unified Ideograph Extension J · Unicode 17.0

此字符收录于 Unicode 17.0 第三表意文字平面扩展J区，目前尚未被大多数系统字体支持。本项目提供完整的跨平台字体包与在线书写器。

*This character is part of Unicode 17.0 CJK Extension J on the Tertiary Ideographic Plane. Most system fonts do not yet support it. This project provides a complete cross-platform font package and online writer.*

**在线体验 · Live site:** https://taforhim.netlify.app

**制作人 · Author:** 栗子饭

---

## 许可证 · Licence

- 字体文件 (`.otf`, `.ttf`, `.mobileconfig`)：[SIL Open Font Licence 1.1](https://scripts.sil.org/OFL) — 见 `LICENSE-OFL`
- 代码文件 (`.html`, `.css`, `.py`)：[MIT Licence](https://opensource.org/licenses/MIT) — 见 `LICENSE`

*Font files are licensed under SIL OFL 1.1. Code files are licensed under MIT.*

---

## 文件说明 · Files

| 文件 | 用途 |
|---|---|
| `index.html` | 在线字形书写器与发布页（用浏览器打开）|
| `SubsetCJK.otf` | 浏览器用单字形子集字体（Stylus 加载用）|
| `u32c3c.user.css` | Stylus 一键安装样式 |
| `fix_names.py` | 字体名称修复脚本（开发用）|
| `_headers` | Netlify CORS 与 MIME 配置 |

字体文件与 iOS 配置文件体积较大，通过 Release 资产分发：

| Release 资产 | 用途 |
|---|---|
| `Patched-NotoSansSC-Regular.otf` | macOS 字体 |
| `Patched-NotoSansSC-Fixed.ttf` | Windows 字体 |
| `Patched-NotoSansSC-Regular.mobileconfig` | iOS 字体配置文件 |

---

## macOS 安装 · macOS Installation

1. 从 [Releases](../../releases/latest) 下载 `Patched-NotoSansSC-Regular.otf`
2. 双击文件 → 点击「安装字体」
3. 安装后无需重启，所有应用自动支持

**输入方式：** 前往「系统设置 → 键盘 → 文字替换」→「+」，「替换为」栏粘贴此字符，「快捷键」填写拼音（如 `ta`），之后在任意应用输入快捷键并按空格即可插入。

*Download `Patched-NotoSansSC-Regular.otf` from Releases. Double-click and click Install Font. Works automatically in all apps after installation.*

---

## Windows 安装 · Windows Installation

Windows 字体回退机制与 macOS 不同，安装字体后不会自动在所有应用中显示此字符，需根据场景分别配置。

1. 从 [Releases](../../releases/latest) 下载 `Patched-NotoSansSC-Fixed.ttf`
2. 右键点击 → 选择「**为所有用户安装**」（必须选此项，普通安装部分应用无法识别）
3. 重启电脑后生效

**浏览器（推荐）：** 安装 Stylus 扩展后，点击发布页的「一键安装 Stylus 样式」按钮，所有网页均可正确显示此字符。注意 Stylus 会替换网页字体为系统字体栈，建议按需在 Stylus 图标中按网站单独开关。

**Word / LibreOffice 等：** 粘贴字符后选中方块部分，手动将字体改为「Noto Sans CJK SC Patched」。

**输入方式：** Windows 无系统级文字替换功能，建议从发布页书写器复制后粘贴使用。

**原生应用（记事本、微信等）：** 暂时无法显示，待 Microsoft 更新系统字体后自动改善。

*Windows font fallback works differently from macOS. Download `Patched-NotoSansSC-Fixed.ttf` from Releases. Right-click → Install for all users. Restart required. Use Stylus for best browser experience.*

---

## iOS 安装 · iOS Installation

> ⚠️ iOS 系统目前对 Unicode 17.0 第三平面字符支持尚不完善，配置文件在原生应用中实际效果有限。建议提前安装，待系统更新后自动生效。

1. 从 [Releases](../../releases/latest) 下载 `Patched-NotoSansSC-Regular.mobileconfig`，或直接在 iPhone Safari 中访问发布页点击安装
2. 打开「设置」→ 顶部「已下载描述文件」→「安装」→ 输入锁屏密码 →「完成」

**从 Mac AirDrop：** 右键 `.mobileconfig` 文件 → 「共享 → AirDrop」→ 选择 iPhone → 前往设置完成安装。

*iOS support for Unicode 17.0 TIP characters is not yet complete. Install now so it works automatically when iOS updates.*

---

## Android

原生 Android 系统目前无法正确显示此字符。建议使用发布页在线书写器进行输入与预览，待 Google 更新系统字体后自动改善。

*Stock Android cannot yet display this character in native apps. Use the online writer at the live site.*

---

## 浏览器 Stylus 样式 · Browser Stylus Style

适用于 macOS 与 Windows 的 Chrome、Firefox、Arc、Edge 等浏览器。

1. 安装 [Stylus 扩展](https://chrome.google.com/webstore/detail/stylus/clngdbkpkpeebahjckkjfobafhncgmne)
2. 访问发布页，点击「一键安装 Stylus 样式」
3. 所有网页均可正确渲染此字符

> ⚠️ Stylus 样式会将所有网页字体替换为系统字体栈，可能影响部分网站排版。建议按需开关。

*Works on Chrome, Firefox, Arc, Edge on macOS and Windows. Note: replaces all webpage fonts with system font stack.*

---

## 在线书写器 · Online Writer

访问 https://taforhim.netlify.app 即可在任意平台的浏览器中正确显示、输入此字符，无需安装任何字体。使用 opentype.js 直接绘制字形矢量路径，完全绕过系统字体渲染限制。

*Visit the live site to use the online writer on any platform. Uses opentype.js to draw glyph vector paths directly, bypassing OS text rendering limitations entirely.*

---

## 贡献 · Contributing

欢迎提交 Issue 或 Pull Request。如你希望为其他 Unicode 17.0 扩展J区字符制作字形并加入本项目，请参考 `fix_names.py` 中的字体修复脚本与发布页的制作流程。

*Issues and Pull Requests welcome. If you'd like to contribute glyphs for other Unicode 17.0 Extension J characters, refer to `fix_names.py` and the workflow documented on the live site.*
