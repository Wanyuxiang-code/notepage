---
title: Home
banner: "/assets/images/banners/man_u.jpg"
layout: home
heading: 'Explore Infinity'
subheading: 'Beyond the Horizon'
---

hello 👋，我是 oldwinter ❄️，一个云计算工程师，写过几万行代码，带过十几人团队。

这里是一座「全开放式，每日更新」的，由原子化的编织而成。目前主要在浇灌这几个领域 ⭕：


既然你诚心诚意地，闯入了我的花园，那我就大发慈悲地，给你一张地图：。

开个玩笑，客官莫怪 😂。虽然有导览，但这绝不是传统的博客，这是我，所以可能有很多看起来令人费解的半成品内容，也会颠覆你传统的长文阅读习惯。当您漫步花园时，这里有 2 个不成熟的小建议 💁：

- 尽量通过鼠标悬浮预览进行[[上下文]]不中断的阅读。
- 尽量通过底部[[反向链接]]找回来时的路。

这座数字花园使用 [[Obsidian]] 写作和发布，且毫无保留地**开源**，这里是，这里是项目地址：[GitHub - yuxiang/notepage](https://github.com/Wanyuxiang-code/notepage.git)。

这座花园里，我挖了很多坑 🕳，如果你想敦促我加速填坑，或有一些建议和问题，欢迎来。或直接在下方自带的评论系统留言。如果方便的话，给个 star⭐️ 呗。

最后，如果您发现了令人不适的内容，或我的个人隐私，请告知我，万分感谢 🦀🦀: yuxiang.23@intl.zju.edu.cn。

---

<strong>🆕 最近创建：</strong>
<ul>
  {% assign recent_notes = site.posts | sort: "date created" | reverse %}
  {% for post in recent_notes  limit: 3 %}
    <li>
      {{ post['date created']}} — <a class="internal-link" href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>


<strong>⏰ 最近更新：</strong>

<ul>
  {% assign recent_notes = site.posts | sort: "date modified" | reverse %}
  {% for post in recent_notes  limit: 3 %}
    <li>
      {{ post['date modified']}} — <a class="internal-link" href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>
