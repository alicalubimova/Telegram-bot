async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends explanation on how to use the bot."""
    await update.message.reply_text("Hi! send a message if you want to have a ctrampoline timetable ")


async def timetable(context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send timetable  message."""
    job = context.job
    await context.bot.send_message(job.chat_id, text=f"Beep! {job.data} your time will start soon!")
    

async def set_timer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Add your name to the queue."""
    chat_id = update.effective_message.chat_id
    try:
        due = float(context.args[0])
        if due < 0:
            await update.effective_message.reply_text("Sorry we can not go back to future!")
            return

        job_removed = remove_job_if_exists(str(chat_id), context)
        context.job_queue.run_once(alarm, due, chat_id=chat_id, name=str(chat_id), data=due)

        text = "Your name has been successfully added to the timetable!"
        if job_removed:
            text += "Old entry deleted."
        await update.effective_message.reply_text(text)

  async def unset(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """delete entry: if user changes their mind."""
    chat_id = update.message.chat_id
    job_removed = remove_job_if_exists(str(chat_id), context)
    text = "Record successfully deleted!" if job_removed else "You don't have an active account."
    await update.message.reply_text(text)

        
        
        
