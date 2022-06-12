function MayoroMenor(){
    var a;
    a = document.getElementById('edad').value;
    if(parseInt(a)>9)
    {
        alert('Su Mascota es mayor tiene '+a*7+ ' años en humano.');
    }
    if(parseInt(a)<9)
    {
        alert('Su Mascota es joven tiene '+a*7+' años en humano.');
    }
}