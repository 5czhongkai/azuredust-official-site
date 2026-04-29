# AzureDust 官网 Vercel 上线包与部署清单

## 1. 上线包边界

Vercel 需要部署的运行文件：

```text
index.html
styles/main.css
scripts/main.js
assets/
```

当前通过 `.vercelignore` 排除以下非运行文件：

- 项目文档：`*.md`、`AGENTS.md`
- 本地预览脚本与缓存：`scripts/preview.py`、`scripts/__pycache__/`
- 设计参考图：`手机端.png`、`桌面端.png`、`logo-primary-dark.png`
- 素材说明文档：`assets/README.md`
- 已保留但页面不引用的源图：`assets/services/services-global-site-v1.png`

## 2. Vercel 项目设置

在 Vercel 创建或导入项目时使用以下设置：

| 项目 | 设置 |
|---|---|
| Framework Preset | Other |
| Root Directory | 当前项目根目录 |
| Build Command | 留空 |
| Output Directory | `.` |
| Install Command | 留空 |

说明：当前官网是纯静态页面，不需要 Node.js 构建流程。

## 3. GitHub 推送准备

本地仓库已经按以下方式准备：

```bash
git init -b main
git add .
git commit -m "Initial AzureDust website"
```

如果你已经在 GitHub 创建空仓库，拿到远程地址后执行：

```bash
git remote add origin git@github.com:<your-account>/<your-repo>.git
git push -u origin main
```

如果使用 HTTPS 地址：

```bash
git remote add origin https://github.com/<your-account>/<your-repo>.git
git push -u origin main
```

建议仓库名：

```text
azuredust-official-site
```

建议先建为 Private，确认上线无误后再按需要改为 Public。

## 4. 上线前最后确认

- `index.html` 可以正常打开
- `styles/main.css` 加载正常
- `scripts/main.js` 加载正常
- `assets/` 中页面引用图片全部存在
- 移动端菜单可打开关闭
- 微信分享图：`assets/share/wechat-share-cover-v1.jpeg`
- favicon：`assets/brand/favicon-32.png`
- Apple Touch Icon：`assets/brand/apple-touch-icon.png`
- 联系信息确认无误：微信、电话、邮箱、地址
- ICP 备案号确认无误

## 5. Vercel 从 GitHub 导入

1. 打开 Vercel Dashboard
2. 点击 Add New Project
3. 选择 GitHub 仓库
4. Framework Preset 选择 `Other`
5. Build Command 留空
6. Output Directory 填 `.`
7. Install Command 留空
8. 点击 Deploy

## 6. 部署后复查

拿到 Vercel 生成的线上地址后，检查：

- 首页是否正常渲染
- 浏览器控制台是否有 404 或 JS error
- 首屏 Hero 图是否加载
- 服务矩阵、行业图、愿景图、联系区图片是否加载
- 移动端宽度下菜单是否正常
- 分享图、favicon、Apple Touch Icon 是否可访问
- 页面上的邮箱、电话、微信、地址、备案号是否正确

## 7. 后续绑定正式域名

如果后续绑定正式域名：

- 在 Vercel 项目的 Domains 中添加域名
- 按 Vercel 提示配置 DNS
- 域名解析生效后用正式域名再跑一次上线后复查
- 如果备案号对应的是中国大陆访问场景，需要确认域名备案主体与实际展示信息匹配
