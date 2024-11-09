---
title: Home
banner: "/assets/images/banners/man_u.jpg"
layout: home
heading: 'Explore Infinity'
subheading: 'Beyond the Horizon'
---

hello 👋! Welcome to Yuxiang's Notepage. This Notepage is designed to share my obsidian notes online, hopefully to provide help and sources of inspirations for u.

Thanks to previous open-source repositories, I can achieve the obsidian features of bidirectional links on online pages.

This notepage is still under construction with some bugs, like the ineffiency of side bars or some math LaTex formula display error. Please don't mind.

This online digital graden is based on my local repository of obsidian, which boasts its high extensibility.

The notepage deployment is fully open-source, if u are interested, u can surf my github repository：[GitHub - yuxiang/notepage](https://github.com/Wanyuxiang-code/notepage.git). 

If u like it , why not give it a star ⭐️


contact email: yuxiang.23@intl.zju.edu.cn

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
