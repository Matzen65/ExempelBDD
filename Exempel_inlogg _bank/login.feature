Feature: Logga in på internetbanken
  Som kund i Nordea vill jag kunna logga in och se mitt saldo.

  Scenario: Användaren loggar in med korrekt användarnamn och lösenord
    Given användaren befinner sig på inloggningssidan
    When användaren anger sitt användarnamn och lösenord
    And klickar på logga in knappen
    Then blir användaren inloggad och kan se saldot

  """
  Scenario: Användaren loggar in med felaktiga uppgifter
    Given användaren befinner sig på inloggningssidan
    When användaren anger Kalle som användarnamn
    And klickar på logga in knappen
    Then visa ett felmeddelande om användarnamn och lösenord


  Scenario: Användaren loggar in med tomma uppgifter
    Given användaren befinner sig på inloggningssidan
    When användaren inte skriver in något alls
    And klickar på logga in knappen
    Then visa ett felmeddelande om användarnamn och lösenord
  """


  #@wip #tagg - work in progress
  #Feature: Inloggning med Outline, ersätter de grönmarkerade ovan

  Scenario Outline: Ogiltiga inloggningar ger fel
  Given användaren befinner sig på inloggningssidan
  When användaren anger "{username}" och "{password}”
  And klickar på logga in knappen
  Then visa ett felmeddelande om användarnamn och lösenord

  Examples:
  | username| password      |
  | kalle   |               |
  |         |               |
  | bandit  | gemigpengarna |
  | jonas   | hemligt       |