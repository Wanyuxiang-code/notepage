---
title: Home
banner: "/assets/images/banners/man_u.jpg"
layout: home
heading: 'Explore Infinity'
subheading: 'Beyond the Horizon'
---

hello 👋! Welcome to Yuxiang's Notepage. I'm a sophomore student major in Electrical and Computer Engineering in Zhejiang University and UIUC. Having passion to shape the world with my own knowledge and dedications, I desire to explore the infinity of myself while also exploring the different dimensions of the world. Join me in this expedition! 

This notepage is designed to share my obsidian notes online, hopefully to provide help and sources of inspirations for you. Thanks to previous open-source repositories, I can achieve the obsidian features of bidirectional links on online pages. You can hover cursor over

It is still under construction with some bugs, like related articles, the ineffiency of side bars or some math LaTex formula display error. Please don't mind.

The notepage deployment is fully open-source, if u are interested, u can surf my github repository：[GitHub - yuxiang/notepage](https://github.com/Wanyuxiang-code/notepage.git). 

If u like it , why not give it a star ⭐️

If you want to know more about me, here is my [academic page](https://wanyuxiang-code.github.io/)
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
