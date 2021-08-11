var message = "Welcome to " + app.name
message += " version " + app.version + "\r\r"

message += "I'm installed in " + app.path.fsName + "\r\r"

message += "You have this much memory available for Adobe Photoshop CC: " +
app.freeMemory + "\r\r"

var documentsOpen = app.documents.length
message += "You currently have " + documentsOpen + " document(s) open.\r\r"

alert(message)

var answer = confirm("Set hte foreground and background to my favorite colors?")
if (answer)
{
    app.foregroundColor.rgb.red = Math.random()*255
    app.foregroundColor.rgb.green = Math.random()*255
    app.foregroundColor.rgb.blue = Math.random()*255
    app.backgroundColor.rgb.red = Math.random()*255
    app.backgroundColor.rgb.green = Math.random()*255
    app.backgroundColor.rgb.blue = Math.random()*255
}

if (app.documents.length == 0)
{
    var sampleDocToOpen = File(app.path + "/Samples/Fish.psd")
    message = "Would you like me to open a sample for you? ("
    message += sampleDocToOpen.fsName
    message += ") "

    answer = confirm(message)
    if (answer)
    {
        open(sampleDocToOpen)
    }
}