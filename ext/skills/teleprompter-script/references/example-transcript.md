# Transcript

Meeting Title: Claude Cowork Workshop

Date: May 12

Meeting participants: Mark Alston

## Opening & Introductions

**Katie (Sonos):** Hi Katie. Hey good morning. I'm wanting to make sure this is recorded. Got it. Okay. I'll give it just maybe a few seconds before we get started -- we've got quite a few people who wanted to attend. But I also know it's a 90 minute session so we want to get into it pretty quickly to make sure that there's time for that. Just let me know when you're ready to kick off and I can kick us off.

Yeah great. I'll give it like another 30 seconds. Chat for a second and then turn it over. See quite a few folks from Forgd here -- it's always so good to see you.

All right, we've got at least half of the folks who I'm planning to attend, so thank you for joining. Thanks to Forgd for leading this workshop. This workshop focuses on Claude Cowork, and so Sonos folks, if you've already been using it or you've been following along in the Claude Slack channels, maybe participated in some of the recent AI lunch and learns, you've sort of seen how maybe your colleagues are using Cowork. You're using Cowork and maybe have gotten a sense of really how remarkable Cowork is -- which might be an understatement, probably need another word for that.

There are a lot of really interesting use cases being shared in terms of personal productivity, actual workflows, and it's all really very exciting -- but also maybe a bit overwhelming if you're not quite sure how to use it, how best to use it. So this session really is meant to be a foundational and approachable session to help you get a better understanding of how Cowork works, when to use it, better ways to use it yourself so we can really all integrate it into our day to day effectively.

As in past sessions, Q&A is available for you in the Zoom chat at any point if you want to ask a question. We've got quite a few folks here from Forgd, a few folks from Sonos as well who can help answer questions. There is a dedicated Q&A at the end as well. And then just a last plug: if you learn about something today and you try it and it's not working, or you've been using it and sort of are stuck -- we do have office hours on Thursday for you to drop by at any point and just pop in and ask your question, or listen to the questions other people have. So with that, I will turn it over to Evan. Thank you all -- this is going to be a really, really good session.

**Evan (Sonos):** Yeah, thank you Katie. You basically did my whole job for me, so I don't have to do that, which I very much appreciate. But again, as she said, we're available to answer questions in the chat and we have the office hours set up on Thursday. So if you learn anything today or you have further questions or you run into a roadblock between today and Thursday, please don't hesitate to bring them up on the office hours. I will hand it off to Mark Bagai, an Applied AI Architect, and Graham Zuloff, Applied AI Architect at Forgd, who are going to run through the session today.

**Mark (Forgd):** All right, hey everybody. Just a quick audio check first -- can you hear me okay? Yep, cool. So Graham and I will be sharing presentation duties today. I'll drive most of the slides and Graham will focus on the demos.

First of all, welcome everyone, it's great to see a lot of people joining. We'll be spending the next 90 minutes talking about Claude Cowork. As Katie said, it really is a super interesting addition to the Claude product family, and we think both from our own perspective at Forgd and certainly also from what we've been learning from customers using it, that it's sort of the interface that particularly every chat user should be looking at next for automation of all those repetitive daily workflows -- and also looking at some of the complex multi-step tasks that span many data sources and formats that you maybe spend a lot of manual time and effort on today.

Graham, are you sharing a deck? I can't see it yet. I think it's better you drive since you're going to be doing the demos. One second. Cool. While Graham does that, maybe let's get a quick thumbs up from everyone who's already using Cowork today. All right, see a bunch there. Cool, that's good. So as said, if you have questions, please ask them in the chat. We've got some of our applied AI architects on the call here today -- I see Greg, Mark on here -- and they're here to help answer questions as they come up.

Next slide please.

## Agenda

**Mark:** All right, so this is the agenda for what we'll cover today. We can also share this deck out if it's useful for anybody to have after the fact, so don't worry if you miss anything here.

The first thing we'll do is dive into a really basic walkthrough of what Cowork is and also how it came to be -- for example, why do we need another product alongside chat and code. Then we'll see Cowork in action with a demo that steps through some of the capabilities. After that in section two through six, we'll cover the building blocks that make up Cowork, and we'll jump back into the demo at various points to see some of those concepts in action. Then we'll close with a little call to action and what's next, and we'll have time for some questions as well.

> _(Mark, transcription noise: "Mark. You can. See. That.")_

## Where Cowork Lives in the Claude Universe

**Mark:** Next slide please. First of all, just a quick map of where Cowork lives in the Claude universe -- that's sort of rapidly expanding and getting built out. I would assume that most of you all are familiar with chat by now, and some of you may also be working in Claude Code daily.

Chat obviously is a conversational interface for Claude that lives either on the website claude.ai or in the desktop app. Code, of course, lives in the terminal in your IDE of choice, if that's how you're consuming it, and also accessible from desktop and web. I'm not sure if you all are using the Chrome extension -- that's another way to use Claude. There are also agents for the Microsoft Office apps. And then we have Cowork, which is what we're talking about today.

It lives in the Claude desktop app and we'll get into why that is. It really is a desktop agent that's built for delegating work, especially long-running tasks that span multiple tools and files.

## What Is Cowork: One-Sentence Definition

**Mark:** Let's go to the next one. So this is kind of the one sentence definition of Cowork that we use. We call it a personal agent that lives on your computer, and we'll spend the next couple of slides unpacking what that means before we get to the demo.

The way I like to think about this is to consider how we got here over the last couple of years. When LLMs launched a few years ago, the predominant and only interface for working with them was through chat. You opened a chat window, wrote a prompt, the model gave you back a response, and you drove every turn of that interaction.

At some point, LLMs evolved to be able to use tools. That means models now had the ability to reach outside themselves and their training knowledge to retrieve information and take action using computer programs. We see this today manifested in the form of connectors to all your other apps, in the ability to execute code and search the web from inside the chat. The shape of the interaction though is still very similar to the early days -- you're driving each turn, writing prompts and getting responses back. But these responses obviously do more with tools.

Today's agentic systems flip that interaction pattern a little bit. Now the model is the one deciding, instead of you directing the model. The model creates a plan, picks the right tools, runs them, checks its work, and keeps iterating like that until it's done. That means you're able to delegate and step away.

That shift -- from you directing the model to you writing the goal and letting the model reason about the steps -- is the difference between a chat and an agent. That agentic foundation is what Cowork is built on. In fact, Cowork shares the agentic infrastructure that powers Claude Code.

The way Cowork came to be, in many ways, is that the Anthropic team realized that developers were using Claude Code for a lot of things that weren't specifically code and software engineering. They were harnessing its general ability to do long-running tasks and use tools to do them. Claude Code brought this capability to developers. Cowork brings the same capability to everyone else, but in a form that's a little bit safer to use for those of us who are not software developers.

## Four Things About "Personal Agent"

**Mark:** Next slide please. Now let's cover quickly what the "personal" part of personal agent means. There are four things here that you should pay attention to.

**First**, Cowork works in a local folder on your computer that you point it to. Cowork can see and modify what's inside that folder, but it can't reach beyond. That's a key security design of Cowork. It's important to keep in mind this is different, for example, from the capabilities you have in Claude Code where you have much broader access to your local system.

> _(Mark, transcription noise: "The 15. Weeks.")_

**Second**, Cowork requires explicit approvals on destructive actions. So if you have a task that involves modifying files and maybe even occasionally deleting information, you'll always get an approval prompt before that happens.

**Third**, Cowork runs as you, with your identity. This is maybe obvious when you think about taking actions on your local computer. Where this is really important to understand is when we talk about using connectors in Cowork tasks. Cowork runs with your identity in Google apps, for example. If you connect to other systems like SaaS apps, it's running with your identity and your permission set. It's not using a service account as you may see if you're using some cloud service. It's running as you.

**Fourth**, all of this runs on your computer, and whatever you do in Cowork only runs as long as your computer is awake. This is not a cloud service. This is teed off your local computer. So if your lid is closed, if your workstation's turned off, Cowork flows will not run.

## Demo 1: Weekly Review Automation

**Mark:** All right, now let's actually flip to a demo. We'll give a little overview of what Cowork looks like in action and then we'll get back to some of the features later. I'll turn it over to Graham here.

**Graham (Forgd):** So many of you are probably just getting to know Cowork, maybe using it for the first time. So just so everyone can kind of be on the same page, let's take a look at the interface so you can see how to access Cowork in the desktop app.

When you launch the desktop app, you're going to see in the upper left hand corner there are three ways to interface with Claude. We have chat, Cowork, and code. To access Cowork, you just click on the tab and it's going to look familiar -- you'll see a prompt box similar to chat.

Let's walk through an example to show the power of Cowork, something you might be able to relate to. If you're like me, your weeks are full -- emails, messages, meetings, projects, interactions one on one to many. Maybe at the end of the week you like to have a little mini retrospective. What is it that I've worked on? What are some areas where I've learned lessons? What are some accomplishments? But also look ahead to the next week -- what are the things I need to focus on?

In order to do that, that takes quite a bit of time. You've got to go across maybe a number of different data sources -- your email, your calendar, maybe a folder you keep your meeting notes in. All of those things might take a while to compile this weekly review. This is where Cowork really shines.

Let's actually work with Cowork here and see how we can help produce this report in a way that's automated. We've prepared a prompt here that we're going to paste into our Cowork box, and I'll walk you through briefly what this prompt does. This is something that you can write yourself, or you can even use Claude chat to help you do it.

We're going to tell Claude Cowork: we want to create this end-of-week review, and we want it to run every Friday. So we've told Cowork this is a scheduled thing.

Now we want to focus on where the places are that we want to pull information from. We're going to pull from our Gmail, our calendar, and also we want Cowork to look in a local folder where we store meeting notes. We've given it the path. We've also told Cowork we don't want certain things included in this weekly review -- maybe things that are private. So if we've marked or labeled something or put it in a folder called private, just ignore that.

Then we tell Cowork how we want this weekly review structured. We want a headline. Tell us the top three wins from the week. Some misses and lessons. Surface any action items we might have personally. If there are any projects we're working on, what's the status? And finally we want to look ahead -- Monday, the week ahead, the next business day. What are my priorities? Is there anything I need to prepare for?

Finally, we tell Claude where we want this weekly review stored and what format we want it in. We've given it a path.

A couple of other things we can see in Cowork: we tell Cowork where to work for this task -- in this case, my Documents folder, because that's where I've stored my weekly notes and where I want to store the output. You can also tell Claude how to prompt you for actions, whether to ask you for permission or just take action without that. And finally, which model to use.

Let's go ahead and execute this prompt. You'll notice a couple of things once we've started. There are a few boxes on the upper right hand corner as Cowork churns away. The first is a progress steps box. You'll also see if there are any documents or instructions that have been given, and any skills it's using for this task.

First we see that it's going to create a plan, load all the skills, use a scheduled task prompt, and then execute. Let's look closer. First, it's reading. Then it's going to create a scheduled task because we told it we wanted it to run every Friday at 3pm. Now it's prompting us -- remember Mark said it'll ask you explicitly whenever it creates actions that change. So we'll approve it. Yes, we want to allow the scheduled task. It sees I already created one before, but it'll create a redundant one here.

Now it's loading the tools to create the scheduled task. This should take just a minute. One interesting thing: as we'll show you later, you have an explicit interface in Cowork for creating scheduled tasks, but you can also just let Claude infer that that's what you want, like we did here, by saying in the prompt that we want it scheduled.

Let's schedule that task. Now it's told us it's created. We have a couple of ways to access this task. Let's go into our Scheduled section in the upper left hand corner. We'll see it's created this new task: end of week review. We can click into it. First, it gives us a brief description. We can also pause or make this task active. We can see here the explicit instructions that Claude Cowork is going to use to achieve the outcome -- the very specific steps it's going to take.

Let's click Run Now and watch this task execute. You'll notice a little notification that it's running. We can also see History. It's going to execute the task steps. First, it's searching for email threads. Listing calendar events. Creating a directory where it will store the output. Now it's churning through some of that data from the mail.

**Mark:** One thing to note, Graham -- I see we're not getting the progress overview here. But if you look at the right side of the screen, this is really where the interface is quite different from the regular chat you're used to. You've got a couple different interesting boxes going from the bottom. You can follow along and see exactly what context elements Cowork is bringing in to execute this task. You'll see the connectors and skills here. Think of connectors as data context -- data from other systems. Think of skills as operational context -- how to do certain things. You'll also see the documents it's pulling in.

There is this progress box up here which is not active right now. Most of the time when you use Cowork, you'll see a breakdown of all the steps that Cowork knows it needs to go through. That's the agentic loop in action -- it actually knows what it means to complete the task and what it needs to go through to get there. One of the big advantages of using Cowork over chat is being able to see that breakdown and know where it is in the execution of a long-running task.

Unfortunately, whether you get this progress indicator or not is a model-level decision. You can't really explicitly control it. The model will decide how to structure the execution. We actually tried to force its hand a little bit using a tip that Anthropic has in their documentation, but for whatever reason it didn't do it this time. Just know that hopefully you'll see actual progress here in this box more than not.

I'll turn it back to Graham. As you can see, it's ripping through Gmail, calendar, all these other sources, and synthesizing all this information.

**Graham:** Yep. It's almost finished -- going to work on producing the PDF report. As Mark said, this right side is really valuable because you can see previous times this task has run. So you can easily click into that. And then all the different files and documents and objects it's going to use. You're aware of how it's actually using information. The connectors and the skills are a valuable reference here.

It's producing the report. Maybe we'll jump over to one that was already produced. Actually, it's creating it now, so we'll wait. Another thing -- if the task starts running and you realize you need to stop it to maybe change the instructions, you can do that right here with the stop button in the prompt box.

This is where it's going to produce the PDF -- it'll output it to this location. You can browse via Finder or Windows Explorer directly. But it'll also produce a link right here when finished.

Looks like I did quite a bit of work this week -- going to be a big report.

**Mark:** It's also interesting to see how much is going on. You've got retrieval from external systems, code execution to build the PDF. If you were doing this manually, some of these steps you'd do differently. There is a lot going on, and you're seeing a lot of the capabilities play out in terms of Claude reasoning about using the right tool to get to your desired outcome.

**Graham:** All right, the report has been produced. Let me make this bigger. It followed the instructions to create a headline, then brought forth the top three wins, misses and lessons from the week. You'll notice after each item it gives a reference -- where did it find that information? Was it in an email? In meeting notes? That way you can quickly find the source.

Okay, Mark, I think we'll hand it back to you.

## Core Capabilities Recap

**Mark:** Let me flip over to the deck. So I think what we saw is a good representation of what Cowork is capable of doing. We see a summary of the core capabilities here, and we saw a lot of these in action.

We talked about **connectors** -- using configured connectors to connect to databases, email, web apps, etc. Under the hood, that's all using MCP. Not really something you need to worry about, but make sure your connectors for the apps you use the most are configured.

**File operations** -- we saw that in Cowork reading notes from our local Documents folder, but also writing that report back to that folder. This is something chat can't do at all -- it's unique to Cowork. Chat doesn't have any capability to read or write documents even in a scoped local space, but Cowork does.

We saw Cowork using **skills**. Skills are instructions that codify how to do a particular workflow or task. You can use built-in skills from Anthropic -- that's what we see when Cowork invokes the skill to create a scheduled task, for example. But you can also have skills you create that encode practices and standards for how you want work done -- personal, departmental, or for all of Sonos.

We also saw the ability to **schedule tasks** and run them recurringly. **Sub-agents** are something you don't necessarily see, but it's part of the power that comes from the same agentic infrastructure that underlies Claude Code. It has the ability to parallelize processes like fetching data from multiple sources to get tasks done faster.

We saw a little bit -- well, I wouldn't call it data analysis since it was just text, but more the reasoning ability to pull data from multiple sources and synthesize information in quite an advanced way. That's a good overview of Cowork's capabilities.

## The Task Loop: Describe, Plan, Approve, Deliver

**Mark:** We'll spend this next part of the presentation going into some of the key concepts you need to understand about how Cowork actually operates so you can use it more effectively. We're going to start with the task loop.

> _(Mark, transcription noise: "So I'm going. To turn it on.")_

Every task that you run in Cowork follows this structure. It's important to understand it as a mental model -- what's your job and what's Cowork's job in this flow.

> _(Mark, transcription noise: "You can. Think of it as. The. Beast.")_

This describe / plan / approve / deliver flow is more or less how every task in Cowork gets executed.

**Describe** is your job. You name the outcome you want, not the steps.

> _(Mark, transcription noise: "Of. The. Un. Iverse.")_

The outcome, for example, is: give me a weekly review with this structure and these action items. How that gets done is Cowork's job.

**Plan**: Cowork breaks down your goal and proposes the steps it'll take. You saw this in the demo -- the plan appeared before the execution started. If you're doing a one-off task in Cowork, it's more integrated. If you're making a scheduled task like we just did, it's sort of plainly split.

**Approve**: If there are actions in the task execution that create, delete, or change things, you'll be asked to approve it. This is also an opportunity for you to revise or steer execution. Nothing destructive ever happens without you seeing it up front and giving an explicit approval.

**Deliver**: Cowork's job is to run the steps, verify it works, and deliver the result to you.

You'll see essentially two different modes of interacting with Cowork. When you are designing task execution and improving it, it'll be this back and forth between you and Cowork. Once you're comfortable with the way it's executing and the outcome it's delivering, you can fully delegate and leave it to execute on its own.

## Demo 2: Iterating on a Task (Adding Granola)

**Mark:** Let's actually step back into our demo and get a feel for what this looks like by making a few changes to the task we just set up.

**Graham:** Okay, remember in our first task, we set up this weekly review to check our email, calendar, and a local folder with notes. Let's build on this task using the task loop Mark described. We're going to give some feedback to Cowork that we want to add an additional source.

Let's say Sonos adopts a new service, maybe Granola or something similar, where meeting notes and transcripts are stored. You see that as a valuable place to pull into your weekly review. There might be details from a meeting you didn't capture but want Cowork to have as context.

Let's go back to the prompt we used to create the scheduled task and tell Cowork: also pull meeting notes from Granola. We're going to tell it to only use this folder, and to skip anything we don't want included.

Now Cowork is going to use that to amend or iterate on the existing scheduled task. It's doing an update -- looking at the steps and understanding how to best add Granola as a data source. Here it's asking my permission. We'll click Update. So now it's updated -- the task is going to pull from four sources. Just to confirm, we can go over to the scheduled task, open it up, and look at the explicit instructions. Sure enough, under sources we see Gmail, calendar, local meeting notes, and now Granola. Each time we run this, it'll fetch those meeting notes via the Granola connector.

**Mark:** Obviously you can make many more customizations. You can have as many turns as you like to enhance and hone task execution to get both the context and output form to where you want it. And the last step Graham showed -- going back to the task definition and seeing how Cowork actually interprets those instructions and structures the prompt for itself -- I always find that a super useful way to enhance my understanding of what's an effective way to communicate with Claude.

## Context: Global Instructions, Projects, Folders

**Mark:** All right, we're going to continue with the foundational building blocks of Cowork. Next we're going to talk about context. Sorry, one second here.

Since most people have been working with LLMs for a while, at least through chat, I'm guessing this is not the first time you hear about context. It is obviously super important to any interaction with a language model. Context is what guides the execution of any task and Cowork as well. The quality of the output will scale directly with the context you give it. You want Cowork to have context about your company, the specific project you're working on, and standards for how you want that work done.

There are different ways to provide context in Cowork. Three levels, from broadest to most focused:

**Global instructions** live in your Cowork settings in the desktop app and apply to every single session. Think of them as your standing preferences for how you like your work done -- default formats, your role, anything Claude should know about you regardless of what you're working on. You set this once and it's active for every Cowork session.

**Projects**. We use projects a lot at Forgd, and hopefully you've started using them in chat. A project is a dedicated workspace with its own instructions, files, and memory. Memory is key here. Claude remembers what it learned from previous tasks in the project and applies that to future runs. Memory is scoped exclusively to the project, so if something's confidential to a particular workstream, it stays there. You can use projects to organize scheduled tasks.

**Folder instructions**. You can also point Cowork directly at a local folder and attach rules specific to that directory. There are various ways for Claude to pick those up. It operates like a project. I suspect we may see convergence between how that all operates in the future, but folders are a little different from projects for now.

## Demo 3: Creating Projects

**Mark:** We wanted to cover how you actually get started with projects, because it's slightly different from chat. There are a couple of ways to do it.

You can create a Cowork project from scratch. What's important to understand is that the project lives on your local computer. It's different from the projects you have in chat -- a wholly different infrastructure. If you create a project directly in Cowork, it'll just be visible inside Cowork and visible to you.

You can also take one of your existing projects from chat and import it to Cowork. That copies the name, instructions, and memories into the Cowork project. Important: that's a one-way copy that puts that information on your local computer. It doesn't stay in sync with the chat project. A little peculiar, but you can tee off a Cowork task from an existing chat project.

Finally, you can just operate in folders.

Graham, can you show the interface for project creation?

**Graham:** Yep. As Mark said, there are three ways to start a new project. To orient you: when you're on your Cowork tab in the desktop app, there's a section on the left top called Projects. Here you'll see all your existing projects. For instance, I have a project called Demo Project One. You can click in, see details, any instructions, scheduled tasks, and any context you've given it -- files or the memory produced from it.

To create a new project, in the upper right hand corner there's the New Project button. You'll be prompted to produce this from three different ways. **Start from scratch** gives you full flexibility -- project name, specific instructions, files, where the project should live. **Import a project**: you'll be prompted to provide the name of an existing project in Claude chat. Click on the little search box, your projects pop up, or type the name. Click one of those projects and it pulls in the name and elements specific to that project. **Use an existing folder**: if you have a folder on your local machine with a set of files and maybe Claude instructions in markdown format, you can select that folder, and it becomes the starting point for your new project.

Mark, back to the presentation.

## Skills, Connectors, and Plugins

**Mark:** Let's continue with skills, connectors, and plugins. These are all really important building blocks of how Cowork actually gets work done.

Skills and connectors should already be familiar to most of you. **Skills** are how you teach Claude a specific way of working -- a process, format, or set of rules in plain language, typically delivered as a markdown file. **Connectors** are how Claude reaches your apps -- Gmail, Slack, Google Drive, calendar, other sources like Granola, the AI note-taking app, or whatever note-taking app you're using at Sonos, maybe Zoom here.

**Plugins** are newer and more specific to Cowork. A plugin is essentially a bundle of skills and connectors -- it can also have sub-agent definitions -- all put together in a single install. Think of it as a role kit: everything Claude needs to do a particular kind of job, packaged up so you don't have to wire the pieces together yourself.

One way to learn about plugins is to look at some Anthropic is shipping right now. There are a bunch that come with Claude Enterprise, and some of them are enabled for your org. Plugins for HR tasks, general productivity, product management, and so forth, bundling together relevant skills for those jobs.

You can also build your own skills and plugins really easily. The easiest thing to look at would be how to create a skill from the work we've already done building this weekly review. Graham, I'll let you show that.

## Demo 4: Turning a Task Into a Skill

**Mark:** Hey Graham, you're muted.

**Graham:** Thanks. Like Mark said, perhaps you have a task you've been using with good success and you want to save or store it and share it as a Claude skill.

Let's go back to our example -- this end-of-week review. We can see all the times we've run it. Let's go to our most recent run and say we feel satisfied with how this task has been running. We want to convert it into a skill.

**Mark:** Think about the scenario -- you've been doing this weekly review, impressing all your coworkers with this super-structured way of looking at how you work. Now somebody else wants that. How do you give it to them easily? You take all the steps you put together, iterated on, and let Claude synthesize that as a skill you can distribute one-on-one by giving them the file, or let your organization distribute centrally.

**Graham:** In this upper section here, you have a drop-down to take actions on this task -- rename, archive, delete. One of them is **Turn Into Skill**. Click that, and it fills in your prompt box: "Turn this task into a skill." Let's give it a couple more instructions to make sure it understands our intent. "I want to make this skill generic enough for my peers to use."

Execute that, and Cowork is going to call a skill itself to create a skill. It's going to interpret my request to create that new skill that others can reuse.

**Mark:** This is something I'd like everyone to take away. Sometimes you read about the capabilities of AI and agents and skills and think, "Okay, that seems to require a lot of knowledge to build those." It doesn't really. Claude has the built-in capability to help you create skills. Whenever you've organically arrived at something that works that you want to codify into know-how for Claude, you just ask Claude to help you create that skill. You don't really need to worry about what it looks like under the hood. If it needs to ask questions, it'll ask -- just like you see here.

**Graham:** Yep, here it wants to clarify some information. "How should peers configure their sources?" We'll take the recommended one so peers can use whatever arbitrary sources they want by using an argument. Click that. "What sources should the generic version pull from?" Let's check off these three. Click Next. "What output format should be the default?" PDF.

Now Claude has enough information to complete the creation of this new skill. It's going to produce a new skill here. As Mark said, this is extremely valuable -- now others within Sonos can leverage the same tasks others are finding success with. It makes sharing your knowledge and experience within Claude very simple and accessible.

**Mark:** One thing you'll note if you follow the Anthropic announcements is that they have a steady cadence of releasing plugins that collect relevant skills for different job functions. There was a big release recently for Claude for Finance that puts together a lot of the skills, connectors, and sub-agent definitions to perform a lot of the common workflows in that space. It's really interesting to see for general knowledge work how more and more tasks are getting captured in these skills. You'll get a lot out of the box from Anthropic, and the admins of your Claude for Enterprise deployment will decide which ones get distributed automatically. You can also think about, as an organization, what you might want to capture in terms of your specific processes and distribute those as organizational skills. We do that quite actively at Forgd -- skills for doc writing standards, branding standards, writing style guides, things like that.

**Graham:** Here's the power of Claude -- it wrote the skill for us. If we had tried to write this skill on our own, it probably would have taken us quite a bit of time and iteration. But notice it's a well-formatted, detailed, portable skill that others can reuse. We can distribute by saving the skill as markdown and sending it to colleagues, or save it so the organization admin can publish it as an organizational skill.

All right, back to the deck.

## Browser & Computer Use (Roadmap)

**Mark:** This is more of a mention to broaden your horizon around what Cowork can do. I'm pretty sure this is not enabled for Sonos, probably for good security reasons. But we saw how Cowork uses connectors to reach into other apps. There's actually a level below that Cowork can drop into if it doesn't have a connector. Say you're asking it to connect to a SaaS app or website for which no connector exists -- Cowork is actually capable of using the Chrome browser to access that website and browse it much like you would. That capability is there.

The reason we mention it is because it traces the path to where this is all going. Browser use is a subset of the general category of computer use. It's very clear Cowork is evolving in the direction of being able to fully use your computer as you would. There are a lot of security considerations that go into whether that ultimately gets turned on for enterprise users. But it's important to understand: when you think about Cowork as this AI coworker you can delegate to, that's where it's going. If you're using Claude in your personal life, maybe with a Pro or Max plan subscription, full computer use is actually available as a research preview right now. Not available in your corporate use at Sonos today, but important for your mental model. Cowork is evolving toward being able to fully use your computer as if it were you. Delegation of capabilities will probably evolve in that direction.

## Scheduled Tasks

**Mark:** All right, one last set of features: scheduled tasks and live artifacts.

We've already spent a bit of time on scheduled tasks, but we'll double-click on it because as you get into automating more task flows with Cowork, you'll probably have a lot of these running at any given time. Graham, can you go back to the scheduled tasks UI in Cowork and go over how you actually manage them?

**Graham:** Sure. A couple of ways to create new scheduled tasks. Let's start with the scheduled interface. On the upper left side of your Cowork view, there's a section called Scheduled, where you'll see all your scheduled tasks. There's a toggle at the top, which is really important -- scheduled tasks can only run when your computer is awake.

> _(Mark, transcription noise: "So you. Re looking for the tracking.")_

If you've closed the lid and it's gone to sleep, Cowork scheduled tasks will not run even if they're scheduled. Your computer has to be on and awake.

We can see all our scheduled tasks here with the schedule associated with each. Let's go into one. We mentioned earlier you can pause a scheduled task or make it active. Click the pencil or edit icon -- you can open up, and at the bottom set the frequency. Options: manual, hourly, daily, weekdays, weekly. You can also select Run at Exact Time. Sometimes scheduled tasks have a slight randomized delay, but if you want to run at an exact minute, check that box.

That's one way to edit and create new scheduled tasks. Click **New Task** and you can provide the prompt and set the time.

There's one other way to create a scheduled task: in the prompt for Cowork, you can use the command `/schedule`.

> _(Mark, transcription noise: "It's. Either way with. You.")_

Then type the name of your scheduled task, when you want it to run, and the description. Cowork will interpret that and create your scheduled task.

**Mark:** Let's also cover how, over in the scheduled section of the left nav, you can see all the runs. The one below, Graham.

**Graham:** Yep, here we have a history of each time the scheduled task is run -- whether manually or triggered by the schedule. Click into those.

> _(Mark, transcription noise: "Being. Taken. From. The.")_

You see a full transcript of that task, when it was run, all the tools used, files used. We can do things we showed earlier -- turn it into a skill.

> _(Mark, transcription noise: "Temple.")_

Move it to a project. Pin it, archive, or delete. Quickly jump to other runs of the scheduled task.

**Mark:** The run history becomes important especially when you have a lot of these running. Maybe the outputs are always perfect, sometimes they're not. The run history is there for you to inspect what actually happened. And you have the chat box -- you can treat each historical run as a chat and interact with it. You can ask it what happened, but you can also make changes. Each run is tied to the scheduled task definition, so they'll all correctly update the underlying task if you make changes.

## Q&A: Updating Scheduled Tasks from Historical Runs

**Question:** Can you go back to the last slide where you were saying that it updates the scheduled task?

> _(Mark, transcription noise: "Gran. Ular unique.")_

If you look at the runs and all -- can you see that again? I don't think I really understood what that means and why that's important.

**Mark:** Yeah. So like an example. Say you're looking at your outputs -- your weekly report -- and something is wrong. It's not the way you want it. But this has just been running in the background. You may use the run history to inspect: when did this divert from what I wanted? All I meant to say is you can go into any historical run of the task and chat with it and make changes, and they'll all refer back to the same task definition. So it doesn't matter if you modify the task based on a run two days ago -- it'll still go back to the correct task definition.

> _(Mark, transcription noise: "Ly.")_

It'll update the task. If you tell it in a few-days-ago run, "update my task definition so that it does X and is shorter," next time it runs, it'll be shorter. Or change the source, or change the output format. You can interact with it from any of those historical runs.

**Questioner:** Thank you.

## Live Artifacts

**Mark:** Alrighty. Next couple of slides -- live artifacts. This is a really cool feature. I don't know if any of you have been using artifacts in chat, but it also exists in Cowork in a slightly different form.

Live artifacts are persistent, interactive HTML artifacts that can be generated for you. They can keep themselves up to date. They can use connectors to load fresh data from your sources. It's a way to go from a text document to a more interactive, more easily consumable format that's better for sharing.

We use them a lot to create dashboards. The capability to use connectors in artifacts is really cool. You can pin them. I use this a lot in Cowork -- I have various Cowork tasks that update a set of dashboards, from really simple ones to, say, a PTO overview that synthesizes all the requests from my team so I can see who's available and when. I use this dashboard capability a lot. I find it easier to use at a glance than reading through a bunch of documents.

Graham, let's take a look.

## Demo 5: Calendar Load Analyzer Live Artifact

**Graham:** Okay, we want to give you an example of what an artifact might be and how you would create and access one. We're going to an example we prepared. What we want to ask Claude Cowork to do is create a live artifact that analyzes our calendar -- maybe we're interested in how we're using our time, if there are trends, if we're spending more time with one team or group than another, the nature of the meetings, how much time we're actually using across our entire calendar in meetings.

I've told Claude Cowork to build a **calendar load analyzer**.

> _(Mark, transcription noise: "Beautiful.")_

I told it to analyze historical information in my Google calendar, how I want this artifact structured, what kind of information, and to look forward to see what's on the calendar.

After I gave that prompt, Cowork went through and built this particular live artifact. It interpreted my request, reached out to my calendar, and created the artifact with a link. It tells me it's live.

Let's look at this. Click on the link -- I pinned it on the left side; it sometimes doesn't load right there. You'll notice I'm loading this live artifact -- it's live, meaning it's actually going to reach out to my calendar when I open this file. It's done the analysis: in the last 30 days, how many hours I've spent in meetings. A nice graphical interface I can interact with by mousing over. Even more granular information.

Where it gets valuable -- "live" -- is this is not a static HTML page. Each time you open it, in the top right corner there's a reload button. Click that, and it reaches out to those data sources, in this case the Google calendar. You can create a live artifact that taps into any number of remote data sources, connectors, or plugins. This gives a refreshed live view of that data.

Any other details on this, Mark?

**Mark:** It's a cool example of how all the capabilities of Claude come together for any kind of usage. What's actually going on here is Claude is generating code -- writing HTML and JavaScript and using some advanced JavaScript stuff to use the connectors. But you don't have to worry about that. It's a way to get really easy-to-use interfaces for these data analysis, data synthesis tasks.

Important: artifacts in Cowork operate a little differently than artifacts in chat. The key difference is these artifacts in Cowork live on your computer and are personal to you. They can't be shared quite yet. From what we understand and what the documentation says, shareable artifacts from Cowork are on the roadmap for Anthropic, so hopefully that comes soon.

One detail I forgot: on your left hand side you can click on Live Artifacts and access all the ones you've produced. There's also a shortcut for dropping directly into a task that creates an artifact as an output.

## Q&A: Validating Live Artifact Code

**Graham:** Any questions there?

**Mark:** There's a question in chat that might be good. Someone was asking: obviously creating live artifacts is very cool, but how is a non-technical user supposed to check the work Claude has generated in that live artifact to make sure the HTML or JavaScript code is doing what it should? It might be risky to make business decisions off these live artifacts if you don't have a way to validate what's happening under the hood.

Yeah, really good question. A couple of things to look at. One is the freshness of the data -- making sure the data you're looking at is actually current. The second is, if you're asking Claude to do analysis -- calculations or synthesis -- you want to make sure that's correct.

A couple of ways: I'll sometimes check these outputs with Claude in a different session. The other thing I'll do is spot check things in the data source system itself. Those are the two primary methods I use. If outputs are more critical, there are ways to create checks -- sometimes we call them evals. We try to build validation steps into the prompts. We use separate chat sessions, maybe with less context, to verify outputs. And we spot check the data sources.

I think Greg mentioned another thing in chat that's really important: citations. Graham had it too in his weekly output report. If you're working with data from sources, you can prompt Claude to be explicit about where it's getting that data from, and use that to audit that it's pulling data from the correct sources. That's probably the method we use most commonly.

**Graham:** Great. Thanks, Mark. Just a time check -- we have about 20 minutes left.

## Security Model Recap

**Mark:** We have one more slide. We've covered security at various points, but since it's such an important topic, it's worth summarizing the security model for Cowork.

**VM isolation.** I guess we didn't talk about this. We said Claude Cowork is built on the same underlying infrastructure that powers Claude Code -- this is true in terms of the agentic harness, how it actually executes tasks. But what's different from Claude Code is that Claude Cowork operates inside a virtual machine. It's a sandboxed environment. Unlike Claude Code, it doesn't have access to your entire computer, just inside that virtual machine.

**Scoped folder access.** You always grant explicit permission to the folder and file scope on your local computer that Claude can access.

**Deletion protection via review gates.** It'll always ask before destructive actions. Specifically for Sonos's use, you can't actually ask it to operate without that approval.

**Network permissions.** Cowork respects network egress permissions set at the administrative level. It can't necessarily reach everything on the internet.

**Local conversation history.** Cowork stores conversation history locally. As of yet, activity is not captured in audit logs or the compliance API. For that reason, if you have workflows that are regulated -- PII, etc. -- check with your administrator and security department before using Cowork.

## Q&A: Security & Credentials

**Question:** Any questions about security? I have one -- can we use Cowork? Yes, we can use Cowork but with guardrails. Cool. Was there another question?

**Question:** I had a quick question. One of my challenges with some of the automation I'm trying to do is I have to enter in network credentials --

> _(Mark, transcription noise: "So.")_

-- or passwords for mobile devices.

> _(Mark, transcription noise: "You know what? That is?")_

Is there a way with Cowork or using this desktop app with Claude Code where I can say, okay, for the next hour, these are my network credentials, these are my mobile credentials -- enter them for me? Right now I'm running into "hey, you know, I know you want to do this, but it's not allowed." But I want to do it anyway.

**Mark:** I'll bump that one to Mark or Graham. Or maybe Michael who's here. How would you handle that? Can you actually do that? Because I think the correct answer is you probably shouldn't.

**Respondent:** I think we all know that, right? But I think the code will do it. I've done it where it'll come up with alarm bells and say "hey, don't do this." It's like, "hey, you can see this anyway, there's an env file with us in there, you can see it anyway" -- and it will kind of do it sometimes. But I think the correct answer is: if it's something you're doing a lot, you might want to think about some sort of MCP solution as a good proxy where you could manage those credentials more securely, using a key store in your operating system and then Claude accesses things through that. That would be a quote-unquote better way to do that rather than giving Claude those credentials.

Keep in mind: Claude is a remote API. If Claude reads it, it is sent over the wire to that API. Anthropic isn't using that to train, they don't persist that data, those kinds of things. But it's something to keep in mind. And I'm sure Sonos's IT security would have an opinion on that as well. MCP would be a way to keep those credentials securely in a key store, with the MCP server accessing them as proxied access.

**Questioner:** Thank you. That'll work.

## Closing & Call to Action

**Mark:** All right, that caps it for the presentation part. What we'd really like to leave you with -- hopefully this has been useful if you didn't know Cowork already, to get you started in terms of understanding how to use it and how it works -- the next step would be looking at: what is the thing that comes to mind for you? What is that workflow that you think Cowork might actually be able to automate and solve for you? Use the structure we went over to think about that. What's the outcome you want? What are the inputs? Anything you can provide to Claude in terms of context that will allow it to produce a really high-quality output.

I'd recommend that's the mental model to use for looking at which tasks you want to automate. Hopefully this presentation has given you some inspiration. We're also available through office hours to help answer questions that come up as you get into Cowork.

We have a little bit of time. If there are more general questions, we can certainly take them.

## Q&A: Trusted Sites, Tableau, Authentication

**Question (Jen):** Sorry, I put one in the chat. Is Claude Cowork already automatically restricted to look at only trusted sites on the internet? Do we have to do something in our prompt to make that happen?

**Mark:** Vasu, correct me if I'm wrong, but I don't believe Claude in Chrome is turned on right now for Sonos. But if it is, or if it does in the future -- I think Jen is asking about network egress in general. Maybe a question for Vasu, whether there are any egress restrictions generally.

**Vasu (Sonos):** We don't have any egress restriction, but Chrome plugins are still turned off. The feature is still in beta. We need to do additional review once the feature is GA.

**Respondent:** Just to tag on -- it is possible to restrict egress. It may not be done, but it is a feature within the core product suite.

**Vasu:** Regarding the security team, I just want to flag: there are additional guidelines we put together. I'd strongly advise everyone to check the Claude Cowork safety guidelines. It primarily flags some of the risks associated with the Cowork feature. I'll post a link in the chat so everyone can see.

**Mark:** Good resource. There's one other question in the chat, Vasu, about a connector with Tableau. Is that something being looked at internally?

**Vasu:** We already enable the Tableau extension. Tableau MCP external is already enabled.

**Mark:** Okay great. So, Deborah, hopefully you'll be able to see that in your Claude desktop application.

**Vasu:** But Tableau has multiple data sources it needs to connect to. The data source might have some restriction. Just want to caveat: the Tableau extension has capability to enter only the credential to connect to Tableau, but Tableau might use different data sources. Not all sources may be connected.

**Mark:** Got it. If it's available as an extension, the way you'd see it is to go into the desktop app, into your settings, and there should be an Extensions tab where you can see installed extensions. There may be a button to browse extensions, and there you should be able to find the Tableau extension. It's a little different than a connector in the sense that the extension is actually an MCP server that gets installed locally on your computer. So just because you don't see it in the connections menu, doesn't mean it's not there.

**Vasu:** Okay cool. So that's how the setup looks. Pattern that, and you should be good to go.

**Respondent:** One quick note on the Tableau MCP server. This is right now really just the connection. It can see a data source. It cannot connect to the underlying data. So it'll just read what you see on the screen. It can download the image or a PDF, and there is no semantic at all in the MCP server yet. So if somebody wants to use it, I'd recommend just using it for exploring, finding some data, but not as the fact right now. We're working on good solutions to have this available in the future.

**Maureen (Sonos):** Mark, can we talk on the authentication again? I know we got a question about entering credentials into Claude.

**Mark:** Yeah, sorry. What were the specific questions?

**Maureen:** I'm on the security side at Sonos and I just want to outline, like you said, that it's not recommended. I also want to call out the fact that in my experience with Cowork, if you have an active session in the browser -- if you've already done that authentication -- it shouldn't be necessary, right? We can leverage the existing cookie and active session.

**Respondent:** Correct, for some things, yes.

**Maureen:** Okay. When you say "some things," what's the asterisk next to that?

**Respondent:** I think actually the browser -- that would apply for connector authentication. So if there's a connector and it uses the general OAuth token, that will work. If it's specifically through the token... I think. Yeah, I've used the Chrome extension personally, not on any of my Sonos. So that's probably more what I'm talking about of it looking at it. If that were available, that would be even more useful.

**Maureen:** Okay. All right. Cool.

**Respondent:** And for anybody on the call looking to use credentials with specifically Claude Code, we have some really good integrations with 1Password for storing and calling SSH credentials. It's like an environmental variable where you don't have to plug it in in plain text. Happy to help anybody looking to explore that further.

**Mark:** Cool, thank you. Do you have a write-up for that anywhere or a link you can provide?

**Respondent:** For the SSH part specifically? No, for the 1Password using an MCP with 1Password for credentials. Let me see what I can find. I can talk to my reps over there to see if they have a KB or something.

**Mark:** Cool, thanks.

**Question (Jen):** Can different connectors be available to different people?

**Vasu:** Connectors are typically enabled at the organizational level, and then you configure the ones you want to use in your instance of Cowork. From the admin-managed connector side, all of them are available for everyone.

**Mark:** Thanks. Yeah, the note on credentials is really good. Probably something we should integrate in the demo, because it's going to be a very frequent topic. Thanks for that feedback.

## Closing Thought: When You Outgrow Cowork

**Mark:** Maybe I'll leave you with one last thought around Cowork, since I think it's such an interesting mode of working with Claude. As you start automating your tasks, what really crystallized in my mind as I've gotten more comfortable with it is two tracks: personal productivity improvements, and automations or productivity improvements that affect how your team operates or how you operate as an organization.

There are a couple of things you may run into as you get more advanced. The first is when you've automated a process to the level where you realize:

> _(Mark, transcription noise: "Maybe.")_

"This would actually be so much better if it was always on and didn't depend on my local workstation." That's a sign you've hit something valuable, and you now need to scale it beyond what's just available on your computer and maybe make it available as a central service to everyone.

Another flavor of that same issue: when you realize the limit in truly automating this workflow is what _I_ can access. For this process to drive automation for the whole company, it needs to access data on behalf of everyone, not just me. Those are examples of reaching the limit of Cowork and needing something else.

The good news: Anthropic has a couple of capabilities here. There's something called **Managed Agents** -- the ability to run agents centrally. There's also the Anthropic SDK. These are things typically worked with by software engineering, so it might not be something you can do yourself, but there's a path to use the work you've done with Cowork and scale it broader. To get there, you'll need to talk to your admins. But the folks at Anthropic are thinking about this, and there's exciting stuff happening to leverage the skills you create with Cowork and scale them to organizational usage.

If there's broader interest, that's something we can talk more about either offline, in office hours, or maybe a separate presentation.

**Vasu:** For Managed Agents, we also need Claude API access or Claude platform access. I'll post the link where anyone should be able to request access.

**Mark:** Great. You already have it -- that's amazing.

**Question:** So with managed agents, they just run behind an API, right? They don't have access back to our local machines or services at all, do they?

**Mark:** That is correct.

**Questioner:** Okay. Because they have a new -- I was watching an intro about the new memory they're building into it with dreaming and stuff. That was pretty interesting.

**Mark:** Yeah, dreaming is a feature. Imagine a managed agent is a lot like a Cowork task that runs centrally on Anthropic servers. The dreaming feature is the capability for those agents to automatically improve themselves based on the run history. The run history for managed agents is very similar to what we saw with Cowork, but it lives on a server instead of on your computer. The space is moving very fast and everything's changing all the time. Even for us, it's hard to keep up. If anybody has questions, please come to the office hours.

## Wrap-up

**Evan:** Great, thank you so much. Just a few notes -- we'll get the recording out, I'll send around the deck as well. So thank you Forgd. If you could send that to me, and David, I can connect with you to share the 1Password info as well. Thank you.

> _(Mark, transcription noise: "It. S been.")_

**Mark:** Yeah, great. Thank you.

**Evan:** Office hours are on calendars now, Thursday, I believe at the same time -- 11:30 Eastern. It'll be recorded in case you can't attend but want to see what others are working through. Thank you everybody. Thank you Forgd for hosting this. Very helpful.

> _(Mark, transcription noise: "A.")_

**Mark:** Talk to you later. Thank you.

**All:** Thanks everybody. Take care. Thanks everyone.
