export type Locale = 'en' | 'zh';

export type AppInfo = {
  slug: string;
  name: string;
  category: 'featured' | 'more' | 'practice';
  platforms: string[];
  icon?: string;
  fallbackIcon?: string;
  appStore?: string;
  microsoftStore?: string;
  help?: string;
  showcaseImages?: Partial<Record<Locale, string[]>>;
  tagline: Record<Locale, string>;
  summary: Record<Locale, string>;
  features: Record<Locale, string[]>;
};

export const apps: AppInfo[] = [
  {
    slug: 'videohero',
    name: 'VideoHero',
    category: 'featured',
    platforms: ['macOS', 'Windows', 'PPT to Video', 'Local AI'],
    icon: '/images/VideoHero.png',
    appStore: 'https://apps.apple.com/cn/app/videohero/id6761481397?l=en-US&mt=12',
    microsoftStore: 'https://apps.microsoft.com/detail/9nk9b1gcp48w?hl=zh-CN&gl=CN',
    help: '/help/videohero/',
    showcaseImages: {
      en: [
        '/images/showcase/videohero/en/screenshot-1.png',
        '/images/showcase/videohero/en/screenshot-2.png',
        '/images/showcase/videohero/en/screenshot-3.png',
        '/images/showcase/videohero/en/screenshot-4.png',
        '/images/showcase/videohero/en/screenshot-5.png',
      ],
      zh: [
        '/images/showcase/videohero/zh/screenshot-1.png',
        '/images/showcase/videohero/zh/screenshot-2.png',
        '/images/showcase/videohero/zh/screenshot-3.png',
        '/images/showcase/videohero/zh/screenshot-4.png',
        '/images/showcase/videohero/zh/screenshot-5.png',
      ],
    },
    tagline: {
      en: 'Turn PowerPoint decks into narrated videos on desktop.',
      zh: '把 PPT 和备注讲稿快速生成讲解视频。',
    },
    summary: {
      en: 'Import a PPTX with its matching PDF, use slide notes as narration, generate AI voiceover and subtitles locally, then export a finished MP4.',
      zh: '导入 PPTX 和同名 PDF，读取每页备注作为讲解词，本地生成 AI 配音、字幕和 MP4 视频。',
    },
    features: {
      en: ['PPT notes to narration', 'AI voiceover', 'Subtitles and SRT export', 'Local processing'],
      zh: ['PPT 备注转讲解词', 'AI 配音', '字幕与 SRT 导出', '本地处理'],
    },
  },
  {
    slug: 'ttsmate',
    name: 'TTSMate',
    category: 'featured',
    platforms: ['macOS', 'Windows planned', 'Text to Speech'],
    icon: '/images/TTSMate.png',
    appStore: 'https://apps.apple.com/app/6752127439',
    help: '/help/ttsmate/',
    showcaseImages: {
      en: [
        '/images/showcase/ttsmate/en/screenshot-1.png',
        '/images/showcase/ttsmate/en/screenshot-2.png',
        '/images/showcase/ttsmate/en/screenshot-3.png',
        '/images/showcase/ttsmate/en/screenshot-4.png',
        '/images/showcase/ttsmate/en/screenshot-5.png',
      ],
      zh: [
        '/images/showcase/ttsmate/zh/screenshot-1.png',
        '/images/showcase/ttsmate/zh/screenshot-2.png',
        '/images/showcase/ttsmate/zh/screenshot-3.png',
        '/images/showcase/ttsmate/zh/screenshot-4.png',
        '/images/showcase/ttsmate/zh/screenshot-5.png',
      ],
    },
    tagline: {
      en: 'Convert text into speech quickly, with a cross-platform roadmap.',
      zh: '快速把文本生成语音，并逐步走向跨平台。',
    },
    summary: {
      en: 'A practical text-to-speech utility for creators, educators, and anyone who needs clean voiceover files without a complicated workflow. Currently focused on macOS, with Windows support planned.',
      zh: '面向创作者、老师和日常语音生成需求的文本转语音工具，让生成旁白文件更直接。当前重点是 macOS，后续规划 Windows 版本。',
    },
    features: {
      en: ['Text-to-speech workflow', 'Voiceover file export', 'Creator-friendly utility'],
      zh: ['文本转语音', '语音文件导出', '适合内容创作者'],
    },
  },
  {
    slug: 'rightclickmate',
    name: 'RightClickMate',
    category: 'featured',
    platforms: ['macOS', 'Windows', 'Context Menu Tools'],
    icon: '/images/RightClickMate.png',
    appStore: 'https://apps.apple.com/app/6757662347',
    microsoftStore: 'https://apps.microsoft.com/detail/9pgcm7zgcs90?hl=zh-CN&gl=US',
    help: '/help/rightclickmate/',
    showcaseImages: {
      en: [
        '/images/showcase/rightclickmate/en/screenshot-1.png',
        '/images/showcase/rightclickmate/en/screenshot-2.png',
        '/images/showcase/rightclickmate/en/screenshot-3.png',
        '/images/showcase/rightclickmate/en/screenshot-4.png',
        '/images/showcase/rightclickmate/en/screenshot-5.png',
        '/images/showcase/rightclickmate/en/screenshot-6.png',
        '/images/showcase/rightclickmate/en/screenshot-7.png',
      ],
      zh: [
        '/images/showcase/rightclickmate/zh/screenshot-1.png',
        '/images/showcase/rightclickmate/zh/screenshot-2.png',
        '/images/showcase/rightclickmate/zh/screenshot-3.png',
        '/images/showcase/rightclickmate/zh/screenshot-4.png',
        '/images/showcase/rightclickmate/zh/screenshot-5.png',
        '/images/showcase/rightclickmate/zh/screenshot-6.png',
        '/images/showcase/rightclickmate/zh/screenshot-7.png',
      ],
    },
    tagline: {
      en: 'Supercharge desktop right-click workflows with practical tools.',
      zh: '让桌面右键菜单和文件操作更高效。',
    },
    summary: {
      en: 'RightClickMate brings 14 practical tools into your desktop context menu and menu bar, covering file creation, path copying, terminal access, batch processing, image utilities, privacy masking, and workspace shortcuts.',
      zh: 'RightClickMate 把 14 个高频桌面工具放进右键菜单和菜单栏，覆盖新建文件、复制路径、打开终端、批量处理、图片工具、隐私遮挡和工作区快捷入口。',
    },
    features: {
      en: [
        'General settings',
        'Favorite folders',
        'Quick apps',
        'Quick new file',
        'Copy path',
        'Open Terminal here',
        'Batch rename files',
        'Batch resize images',
        'Privacy Eraser',
        'Quick image annotation',
        'Copy to folder',
        'Copy directory tree',
        'Zen Desktop for recording and presentations',
        'Format conversion',
      ],
      zh: [
        '通用设置',
        '常用目录',
        '快捷应用',
        '快速新建文件',
        '一键复制路径',
        '在当前位置打开终端',
        '批量修改文件名',
        '批量调整图片尺寸',
        '隐私橡皮擦',
        '图片快速标注',
        '文件复制到指定目录',
        '复制目录树',
        '禅桌面（录屏 / 演讲模式）',
        '格式转换',
      ],
    },
  },
  {
    slug: 'daydayup',
    name: 'DayDayUp',
    category: 'more',
    platforms: ['iOS', 'iPadOS', 'Widgets'],
    icon: '/images/DayDayUp.png',
    appStore: 'https://apps.apple.com/app/6752538298',
    tagline: {
      en: 'A daily quote companion for steady personal growth.',
      zh: '每日格言与个人成长小工具。',
    },
    summary: {
      en: 'Display inspiring quotes as widgets, import custom quote collections, and keep useful words close at hand.',
      zh: '用桌面小组件展示每日格言，也可以导入自己的语录合集。',
    },
    features: {
      en: ['Daily quotes', 'Widgets', 'Custom quote collections'],
      zh: ['每日格言', '桌面小组件', '自定义语录合集'],
    },
  },
  {
    slug: 'gongke',
    name: '功课助手',
    category: 'practice',
    platforms: ['iOS'],
    icon: '/images/GongKe.png',
    appStore: 'https://apps.apple.com/cn/app/%E5%8A%9F%E8%AF%BE%E5%8A%A9%E6%89%8B/id6639604349',
    tagline: {
      en: 'A practice tracker for daily spiritual routines.',
      zh: '现代人修行的发愿、功课记录工具。',
    },
    summary: {
      en: 'A quiet companion for organizing and tracking daily practice sessions.',
      zh: '帮助记录每日功课、发愿和修行安排。',
    },
    features: {
      en: ['Practice records', 'Daily routines', 'Simple tracking'],
      zh: ['功课记录', '每日安排', '简洁追踪'],
    },
  },
  {
    slug: 'songjing',
    name: '诵经助手',
    category: 'practice',
    platforms: ['iOS'],
    icon: '/images/SongJing.png',
    appStore: 'https://apps.apple.com/app/6448427701',
    tagline: {
      en: 'A chanting companion with a focused reading experience.',
      zh: '专注诵经体验的辅助工具。',
    },
    summary: {
      en: 'Designed to make scripture reading and chanting calmer and easier to continue.',
      zh: '为日常诵经与持续练习设计的安静辅助工具。',
    },
    features: {
      en: ['Chanting support', 'Focused reading', 'Simple interface'],
      zh: ['诵经辅助', '专注阅读', '简洁界面'],
    },
  },
  {
    slug: 'nianfo',
    name: '念佛助手',
    category: 'practice',
    platforms: ['iOS'],
    icon: '/images/NianFo.png',
    appStore: 'https://apps.apple.com/app/6448988399',
    tagline: {
      en: 'Stay focused during mantra recitation.',
      zh: '帮助你在念佛时保持专注。',
    },
    summary: {
      en: 'A lightweight tool for focused recitation and simple daily tracking.',
      zh: '用于念佛计数、专注练习和日常记录的小工具。',
    },
    features: {
      en: ['Recitation focus', 'Daily tracking', 'Minimal design'],
      zh: ['念佛专注', '日常记录', '简洁设计'],
    },
  },
  {
    slug: 'baichan',
    name: '拜忏助手',
    category: 'practice',
    platforms: ['iOS'],
    icon: '/images/BaiChan.png',
    appStore: 'https://apps.apple.com/app/6473900841',
    tagline: {
      en: 'A structured helper for repentance practice.',
      zh: '每日三省吾身的拜忏辅助工具。',
    },
    summary: {
      en: 'A small companion for structured repentance sessions and practice records.',
      zh: '用于拜忏练习、过程记录和自我提醒的小工具。',
    },
    features: {
      en: ['Structured sessions', 'Practice records', 'Quiet interface'],
      zh: ['结构化练习', '过程记录', '安静界面'],
    },
  },
];

export function getApp(slug: string) {
  return apps.find((app) => app.slug === slug);
}
