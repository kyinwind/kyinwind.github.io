import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

const videoHeroItems = [
  { label: 'Introduction', slug: 'help/videohero' },
  { label: 'Settings', slug: 'help/videohero/settings' },
  { label: 'Talking-head Video Repair', slug: 'help/videohero/talking-head-video-repair' },
  { label: 'How to Import Models', slug: 'help/videohero/import-models' },
  { label: 'Voice Cloning', slug: 'help/videohero/voice-cloning' },
];

const rightClickMateItems = [
  { label: 'Overview', slug: 'help/rightclickmate' },
  { label: 'Feature Overview', slug: 'help/rightclickmate/feature-overview' },
  { label: 'General Settings', slug: 'help/rightclickmate/general-settings' },
  { label: 'Favorite Folders', slug: 'help/rightclickmate/favorite-folders' },
  { label: 'Quick Apps', slug: 'help/rightclickmate/quick-apps' },
  { label: 'Quick New File', slug: 'help/rightclickmate/quick-new-file' },
  { label: 'Copy Path', slug: 'help/rightclickmate/copy-path' },
  { label: 'Open Terminal', slug: 'help/rightclickmate/open-terminal' },
  { label: 'Batch Rename Files', slug: 'help/rightclickmate/batch-rename-files' },
  { label: 'Batch Resize Images', slug: 'help/rightclickmate/batch-resize-images' },
  { label: 'Privacy Eraser', slug: 'help/rightclickmate/privacy-eraser' },
  { label: 'Quick Image Annotation', slug: 'help/rightclickmate/quick-image-annotation' },
  { label: 'Copy to Folder', slug: 'help/rightclickmate/copy-to-folder' },
  { label: 'Copy Directory Tree', slug: 'help/rightclickmate/copy-directory-tree' },
  { label: 'Zen Desktop', slug: 'help/rightclickmate/zen-desktop' },
  { label: 'Format Conversion', slug: 'help/rightclickmate/format-conversion' },
  { label: 'Q&A', slug: 'help/rightclickmate/qa' },
  { label: 'Release Notes', slug: 'help/rightclickmate/release-notes' },
];

const ttsMateItems = [
  { label: 'Overview', slug: 'help/ttsmate' },
  { label: 'Main Interface', slug: 'help/ttsmate/main-interface' },
  { label: 'TTS Settings', slug: 'help/ttsmate/tts-settings' },
  { label: 'Pronunciation Dictionary', slug: 'help/ttsmate/pronunciation-dictionary' },
  { label: 'Two-Person Dialogue Split', slug: 'help/ttsmate/two-person-dialogue-split' },
  { label: 'Multi-Person Dialogue Generation', slug: 'help/ttsmate/multi-person-dialogue-generation' },
];

const zhVideoHeroItems = [
  { label: 'VideoHero 介绍', slug: 'zh/help/videohero' },
  { label: '设置页面', slug: 'zh/help/videohero/settings' },
  { label: '口播视频修复', slug: 'zh/help/videohero/talking-head-video-repair' },
  { label: '如何导入模型', slug: 'zh/help/videohero/import-models' },
  { label: '模拟原声', slug: 'zh/help/videohero/voice-cloning' },
];

const zhRightClickMateItems = [
  { label: '首页', slug: 'zh/help/rightclickmate' },
  { label: '功能介绍一页纸', slug: 'zh/help/rightclickmate/feature-overview' },
  { label: '通用设置', slug: 'zh/help/rightclickmate/general-settings' },
  { label: '常用目录', slug: 'zh/help/rightclickmate/favorite-folders' },
  { label: '快捷应用', slug: 'zh/help/rightclickmate/quick-apps' },
  { label: '快速新建文件', slug: 'zh/help/rightclickmate/quick-new-file' },
  { label: '一键复制路径', slug: 'zh/help/rightclickmate/copy-path' },
  { label: '在当前位置打开终端', slug: 'zh/help/rightclickmate/open-terminal' },
  { label: '批量修改文件名', slug: 'zh/help/rightclickmate/batch-rename-files' },
  { label: '批量调整图片尺寸', slug: 'zh/help/rightclickmate/batch-resize-images' },
  { label: '隐私橡皮擦', slug: 'zh/help/rightclickmate/privacy-eraser' },
  { label: '图片快速标注', slug: 'zh/help/rightclickmate/quick-image-annotation' },
  { label: '文件复制到指定目录', slug: 'zh/help/rightclickmate/copy-to-folder' },
  { label: '复制目录树', slug: 'zh/help/rightclickmate/copy-directory-tree' },
  { label: '禅桌面', slug: 'zh/help/rightclickmate/zen-desktop' },
  { label: '格式转换', slug: 'zh/help/rightclickmate/format-conversion' },
  { label: '常见问题', slug: 'zh/help/rightclickmate/faq-list' },
  { label: '更新历史', slug: 'zh/help/rightclickmate/release-notes' },
];

const zhTtsMateItems = [
  { label: '首页', slug: 'zh/help/ttsmate' },
  { label: '主要界面', slug: 'zh/help/ttsmate/main-interface' },
  { label: 'TTS 设置', slug: 'zh/help/ttsmate/tts-settings' },
  { label: '发音字典', slug: 'zh/help/ttsmate/pronunciation-dictionary' },
  { label: '双人对话拆分', slug: 'zh/help/ttsmate/two-person-dialogue-split' },
  { label: '多人对话语音生成', slug: 'zh/help/ttsmate/multi-person-dialogue-generation' },
  { label: '文档格式要求', slug: 'zh/help/ttsmate/document-format-requirements' },
];

export default defineConfig({
  site: 'https://kyinwind.github.io',
  vite: {
    cacheDir: './.vite',
  },
  integrations: [
    starlight({
      title: 'MichaelDev Help Center',
      description: 'Help docs for MichaelDev apps.',
      social: [
        {
          icon: 'github',
          label: 'GitHub',
          href: 'https://github.com/kyinwind',
        },
      ],
      customCss: ['./src/styles/starlight.css'],
      sidebar: [
        {
          label: 'Help Center',
          items: [{ label: 'Overview', slug: 'help' }],
        },
        {
          label: 'VideoHero',
          items: videoHeroItems,
        },
        {
          label: 'RightClickMate',
          items: rightClickMateItems,
        },
        {
          label: 'TTSMate',
          items: ttsMateItems,
        },
        {
          label: '中文帮助',
          items: [
            { label: '帮助中心首页', slug: 'zh/help' },
            {
              label: 'VideoHero',
              items: zhVideoHeroItems,
            },
            {
              label: 'RightClickMate',
              items: zhRightClickMateItems,
            },
            {
              label: 'TTSMate',
              items: zhTtsMateItems,
            },
            {
              label: '诵经助手',
              items: [
                { label: '首页', slug: 'zh/help/songjing' },
                { label: '常见问题', slug: 'zh/help/songjing/faq' },
              ],
            },
          ],
        },
      ],
    }),
  ],
});
