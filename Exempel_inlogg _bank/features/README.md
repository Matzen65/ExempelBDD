# Testa formulär
tap-ht24-testverktyg.github.io/form-demo/
se på DEL3 i föreläsning för resten av koden...

## user stories

[U1] Som en besökare vill jag bli påmind med ett vänligt
felmeddelande om jag inte skrivit i mitt namn, så att jag 
fyller i formuläret korrekt.

[U2] Som en besökare vill jag kunna registrera mig genom 
att klicka på knappen när jag fyllt i alla fält korrekt,
så att jag kan använda tjänsten.


# Acceptanskriterier

[A1.1] Om namnfältet är tomt, ska det visas ett felmeddelande.
[A1.2] Om namnfältet innehåller minst 1 tecken ska felmeddelande inte visas.

[A2.1]Knappen ska gå att klicka på när alla fält är korrekt ifyllda.
[A2.2]Knappen ska inte gå att klicka på om minst ett fält är felaktigt ifyllt.

## Testcenarier
[T1]
1. Kontrollera att textfältet inte är tomt
2. Kontrollera att  felmeddelandet inte visas.
3. Sudda det som finns i fältet
4. Kontrollera att felmeddelandet visas

[T2]
1. Kontrollera att knappen är avstängd. (disabled)
2. Skriv in password i lösenordsfältet.
3. Sudda ut det som finns i fältet.
4. Kontrollera att felmeddelandet visas.

## Headed/headless
För att köra testen i  headless... se föreläsning DEL 3 kl 16:02
För att köra testen i webbläsaren, lägg till en fil med namnet 
`pytest.ini:` i projektets rotmapp:

```
[pytest]
addopts = --headed
```