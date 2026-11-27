// 注意：本文件被 deploy.yml 复制到 .quartz-runtime/quartz.config.ts，
// 故 import 必须使用相对路径（Quartz 未发布到 npm）。
import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

/**
 * Quartz v4 站点配置 · MK_Base
 *
 * 关键约定：
 *  · 公式以 LaTeX 源码存储，构建期 KaTeX 渲染（`Latex` 插件）
 *  · Cloudflare Web Analytics 通过 beacon token 接入（无 Cookie）
 *  · 全文检索使用 Quartz 内置 Flexsearch（500 条后重新评估）
 */
const config: QuartzConfig = {
  configuration: {
    pageTitle: "MK_Base · 数学专业知识库",
    pageTitleSuffix: "",
    enableSPA: true,
    enablePopovers: true,
    // Quartz 4.5+ 未内置 cloudflare provider；
    // 改由 Cloudflare Pages 项目设置中的 "Web Analytics" 开关自动注入 beacon
    // （无 Cookie，符合 PROJECT.md 隐私承诺）。
    analytics: null,
    locale: "zh-CN",
    baseUrl: "mk-base.pages.dev",
    ignorePatterns: [
      "private",
      "templates",
      "_templates",
      ".obsidian",
      "scripts",
      "node_modules",
    ],
    defaultDateType: "modified",
    theme: {
      fontOrigin: "googleFonts",
      cdnCaching: true,
      typography: {
        header: "Noto Serif SC",
        body: "Noto Sans SC",
        code: "JetBrains Mono",
      },
      colors: {
        // 学院深蓝 + 古书烫金 · 适配数学知识库的"沉静学术"基调
        lightMode: {
          light: "#fbfaf7",
          lightgray: "#e5e2da",
          gray: "#b0aaa0",
          darkgray: "#3d3d3d",
          dark: "#1a1a1a",
          secondary: "#1e3a5f",
          tertiary: "#c9a961",
          highlight: "rgba(30, 58, 95, 0.10)",
          textHighlight: "#f4d35e88",
        },
        darkMode: {
          light: "#161618",
          lightgray: "#2a2a2c",
          gray: "#646464",
          darkgray: "#d4d4d4",
          dark: "#ebebec",
          secondary: "#9bb6d6",
          tertiary: "#d4b675",
          highlight: "rgba(155, 182, 214, 0.15)",
          textHighlight: "#d4b67566",
        },
      },
    },
  },
  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.CreatedModifiedDate({ priority: ["git", "filesystem"] }),
      Plugin.SyntaxHighlighting({
        theme: { light: "github-light", dark: "github-dark" },
        keepBackground: false,
      }),
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.TableOfContents(),
      Plugin.CrawlLinks({ markdownLinkResolution: "shortest" }),
      Plugin.Description(),
      Plugin.Latex({ renderEngine: "katex" }),
    ],
    // 不启用 RemoveDrafts —— 项目用 status: draft/review/stable 表达条目成熟度，
    // 全部应在站点上可见（draft 仅是工作流标识，不是内部草稿）。
    filters: [],
    emitters: [
      Plugin.AliasRedirects(),
      Plugin.ComponentResources(),
      Plugin.ContentPage(),
      Plugin.FolderPage(),
      Plugin.TagPage(),
      Plugin.ContentIndex({ enableSiteMap: true, enableRSS: true }),
      Plugin.Assets(),
      Plugin.Static(),
      Plugin.Favicon(),
      Plugin.NotFoundPage(),
    ],
  },
}

export default config
